import ipywidgets as widgets

def get_compounds(element,data):
    """
    for the given element, get_compounds returns compounds that contain that element.
    
    Parameters
    ----------
    element: String
    
    my_data: dictionary
        contains 3 elements (key)
        W/in each element:
             oxides, acids, and salts (key)
             list of compounds (values of ^keys)
    """
    
if data is None:
         data = my_data
     
return data[element]
	
#def get_compound_choice(compound_choice):
	
	
def create_element_select(options=None,description='Element:',**kwargs):
    """
    create a dropdown selector of elements
    
    Parameters
    ----------
    options : list (default None)
        list of elements.  If None, populate with defaults
        
    value : str (default None)
        default value of Dropdown.  If None, do nothing
        
        
    description : str
        descriptive text
        
    Return
    ------
    output : Dropdown widget
    """
    
    
    if options is None:
        options = ['Al', 'Zn', 'Fe']
        
    return widgets.Dropdown(options=options,description=description,**kwargs)
    
    
    
def create_compound_select(options = None, description = 'Compound:',**kwargs):
	"""
	create a dropdown selector of compounds that correspond to chosen element
	
	Parameters
	----------
	options : list (default None)
		list of compounds
	value : str (default None)
	
	description: str
	
	Return
	------
	output : Dropdown widget
	"""
	
	if options is None:
		options = ['Oxides', 'Salts', 'Acids']
	
	return widgets.Dropdown(options=options, description=description,**kwargs)
	
#def create_weightfraction_select(description = 'Weight Fraction:',**kwargs):
	"""
	create a textbox that allows user to input the weight fraction they wish to work with
	
	Parameters
	-----------	
	description : str
	
	value : float
	
	Return
	------
	output : Textbox widget
	"""
#attempted to use the method we discussed earlier with a textbox, unsure how b/c no options for textbox!


weight_fraction_select = widgets.Text(
	description = 'Weight Fraction: ',
	value = '',
	)
	
float(weight_fraction_select.value)

mini_weight_fraction = widgets.Text(
	description = 'Minimum Weight Fraction: ',
	value = '',
	)
	
float(mini_weight_fraction.value)
	
maxi_Weight_fraction = widgets.Text(
	description = 'Maximum Weight Fraction: ',
	value = '',
	)
	float(maxi_weight_fraction.value)






	
	
	
	
	
	