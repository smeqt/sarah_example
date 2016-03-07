import ipywidgets as widgets
from IPython.display import clear_output, HTML, display, Javascript
import pandas as pd

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
    


class component_row(object):
    """
    create a row
    """    
    
    def __init__(self):
                
        
        #elemenets
        #self._element = widgets.Dropdown(options=['','a','b','c'],value='',description='Element:',width=20)
        self._element = widgets.Select(options=['a','b','c'],height=60,width=50)
        
        #blank compound list
        self._compound = widgets.Dropdown(options=[],description=' Compound ',width=180)
        
        #blank mass fraction
        self._massfrac = widgets.BoundedFloatText(description=' mass frac:',width=75,min=0.,max=1.)
        
        #blank min
        self._massfrac_min = widgets.BoundedFloatText(description=' min:',width=75,min=0.,max=1.)
        
        #max
        self._massfrac_max = widgets.BoundedFloatText(description=' max:',width=75,min=0.,max=1.)

        for x in ['element','compound','massfrac','massfrac_min','massfrac_max']:
            getattr(self,'_'+x).margin = 0
        
        
        #monitor element
        self._element.observe(self.populate_compound)
        self._box = widgets.HBox()
        self._box.children = (self._element,self._compound,self._massfrac,self._massfrac_min,self._massfrac_max)
        
    def populate_compound(self,sender,*args,**kwargs):
        
        v = self.element
        out = None
        if v=='a':
            out = [1,2,3]
        elif v =='b':
            out = [10,20,30]
        elif v == 'c':
            out = [100,200,300]
            
        if out is not None:
            self._compound.options = list(map(str,out))
        
        
    @property
    def element(self):
        return self._element.value
    
    @property
    def compound(self):
        return self._compound.value
    
    @property
    def massfrac(self):
        return self._massfrac.value
    
    @property
    def massfrac_min(self):
        return self._massfrac_min.value
    
    @property
    def massfrac_max(self):
        return self._massfrac_max.value
    
    def display(self):
        return self._box


    def to_dict(self):
        return dict(element=self.element,compound=self.compound,massfrac=self.massfrac,massfrac_min=self.massfrac_min,massfrac_max=self.massfrac_max)
        


class component_row_del(component_row):

    def __init__(self):
        component_row.__init__(self)
        
        self._button_del = widgets.Button(description='delete',width=30)
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

