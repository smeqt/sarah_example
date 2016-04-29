import ipywidgets as widgets
from IPython.display import clear_output, HTML, display, Javascript
import pandas as pd
import periodictable as PT

from suggester_interface import get_compound_list


### GET_FORMULA NEEDS TO BE FROM ON_CLICK!!!!!!!!!!!

cells_visable = True
def toggle_code_cells(btn):
    global cells_visable
    if cells_visable:
        display(Javascript("$('div.input').hide();"))
        btn.description = "Show Code Cells"
    else:
        display(Javascript("$('div.input').show();"))
        btn.description = "Hide Code Cells"
    cells_visable = not cells_visable

def run_all(ev):
    display(Javascript('IPython.notebook.execute_cells_below()'))

run_button = widgets.Button(description="Create next input")
run_button.on_click(run_all)
    

toggle_btn = widgets.Button(description="Hide Code Cells")
toggle_btn.on_click(toggle_code_cells)

def init():
    display(run_button)
    display(toggle_btn)



_global_element_list = [str(v) for k,v in PT.elements._element.iteritems() if k>0]



class component_row(object):
    """
    create a row
    """    
    
    def __init__(self):
                
        
        #elemenets
        #self._element = widgets.Dropdown(options=['','a','b','c'],value='',description='Element:',width=20)
        self._element = widgets.Select(options=_global_element_list,height=60,width=50)

        #compound_type
        self._compound_type = widgets.Dropdown(options=['acid','oxide','salt','all'],description='Type:',width=100)
        
        #blank compound list
        self._compound = widgets.Dropdown(options=[],description='Compound:',width=180)
        
        self._choose_button = widgets.Button(description='Choose',width=30)
        self._choose_button.on_click(self._add_formula)

        #NOTE: you forgot to have self._formula be anything!
        self._formula = widgets.Text(description='Formula:',width=180)
        
        
        #monitor element
        self._element.observe(self.populate_compound)
        self._compound_type.observe(self.populate_compound)
        
        #self._compound.observe(self.get_formula)

        
        self._box = widgets.HBox()
        self._box.children = (self._element,self._compound_type,self._compound,self._choose_button,self._formula)
        
    def populate_compound(self,sender,*args,**kwargs):
        
        element_name  = self.element
        compound_type = self.compound_type
        
        out = get_compound_list(element_name,compound_type)
        
        #out = [element_name,compound_type]
        if out is not None:
            self._compound.options = list(map(str,out))
    
    def _add_formula(self,*args,**kwargs):
        formula_val = self._compound.value
        self._formula.value = formula_val

        #NOTE: this needed to be in init, not here!
        #if here, we keep creating a new instance which isn't part of self._box!
        #self._formula = widgets.Text(description='Formula:',width=50)
        
        for x in ['element','compound']:

            getattr(self,'_'+x).margin = 0
        #?
        
        
    @property
    def element(self):
        return self._element.value

    @element.setter
    def element(self,val):
        self._element.value = val


    @property
    def compound_type(self):
        return self._compound_type.value

    
    @property
    def compound(self):
        return self._compound.value
        
    @property
    def formula(self):
    	return self._formula.value

    
    def display(self):
        return self._box


    def to_dict(self):
        return dict(element=self.element,formula=self.formula)
        


class component_row_del(component_row):

    def __init__(self):
        component_row.__init__(self)
        
        self._button_del = widgets.Button(description='Delete',width=30)
        #(x) != (x,)
        self._box.children = self._box.children + (self._button_del,)
        
        

class mult_rows(object):
    
    def __init__(self,ncomp=0):
        self._ncomp = widgets.Text(description='# comp:',value='0',width=50)
        self._ncomp.on_submit(self.update_rows)

        self._button_add = widgets.Button(description='add')
        self._button_add.on_click(self._click_button_add)

        # self._button_del = widgets.Button(description='delete')
        # self._button_del.on_click(self._click_button_del)

        self._head = widgets.HBox(children=(self._ncomp,self._button_add))#,self._button_del))
        
        #intial box setup
        self._rows = []
        self._ring = []

        self._box = widgets.VBox()
        

        self.ncomp = ncomp
        self.update_rows()
        self.update_box()


    def __getitem__(self,i):
        return self._rows[i]

    @property
    def ncomp(self):
        try:
            v = int(self._ncomp.value)
        except:
            v = None
        return v

    @ncomp.setter
    def ncomp(self,val):
        self._ncomp.value = str(val)

    @property
    def nrow(self):
        return len(self._rows)


    def new_row(self):
        if len(self._ring)>0:
            return self._ring.pop()
        else:
            new = component_row_del()
        return new
    
    def add_row(self):
        #from ring?
        new = self.new_row()
        self._rows.append(new)
        new._button_del.on_click(self._click_button_del_row)
        

    def pop_row(self,index=-1):
        row = self._rows.pop(index)
        self._ring.append(row)
        
        
    def update_rows(self,*args):
        v = self.ncomp
        if v is None:
            return

        while self.nrow<self.ncomp:
            self.add_row()

        while self.nrow>self.ncomp:
            self.pop_row()
        
        self.update_box()

    def _click_button_add(self,*args):
        self.ncomp = self.ncomp + 1
        self.add_row()
        self.update_box()

    def _click_button_del(self,*args):
        if self.ncomp>0:
            self.ncomp = self.ncomp -1
            self.pop_row()
            self.update_box()

    def _click_button_del_row(self,d):
        L = [r._button_del for r in self._rows]
        index = L.index(d)
        self.ncomp = self.ncomp - 1
        self.pop_row(index)
        self.update_box()
        
    def update_box(self):
        L = [self._head] + [r._box for r in self._rows] 
        self._box.children = tuple(L)

    def display(self):
        return self._box    

    def to_df(self):
        return pd.DataFrame([x.to_dict() for x in self])

