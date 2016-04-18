import pandas as pd
import suggester
 reload (suggester)

#df_oxides = pandas.read_csv('./data/oxide.cvs')
#df_salts = pandas.read_csv('./data/salt.csv')


#unique_elements_oxides = df_oxides.Target.unique()
#unique_elements_salts = df_salts.Target.unique()

import combo_widgets
reload (combo_widgets)

compound_information = combo_widgets.mult_rows(5)
compound_information.display

#Placement of combo_widgets/compound_information?

def get_element(element):
#Create function that prompts user to input target element

#Parameters
#----------
#
#element: str
#
#entered through widget (Select)

	return element
	
select_target_element = widgets.Select(
	options=[element_list],height=60,width=50)
	
#get_element(select_target_element.value)

def get_compound_type(compound_type):

	return df_compound_type
	#???
select_compound_type = widgets.Dropdown(
	options = ['Acids', 'Oxides', 'Salts'],
	value = '',
	description = 'Type of Compound: '
)

#get_compound_type(select_compound_type.value)

df_oxides = pd.read_csv('./data/oxide.csv')
df_salts = pd.read_csv('./data/salt.csv')

unique_elements_oxides = df_oxides.Target.unique()
unique_elements_salts = df_salts.Target.unique()

def get_compound(df, compound):
	return df[df['Compound:']==element.Formula.unique()

#get_compound(select_target_element.value,select_compound_type.value)

_Global_Suggester == suggester.CompoundSuggester()

def get_compound_list(target_element,compound_type,S=None):
	"""
	Given target element and desired compound type, return list of known compounds
	
	Parameters
	-----------
	target_element : str
		name of target element to query
	compound_type : str
		type of compound to return
		must be one of ['acid', 'oxide', 'salt', 'all']
	S : CompoundSuggester or None
		CompoundSuggester to query. If None, use default suggester
		
	Returns
	-------
	out : list
		list of compounds of desired type and target element
	"""
	if S is None:
		S = _Global_Suggester
	elif compound_type == 'acid':
		df = S.acid
	elif compound_type == 'oxide':
		df = S.oxide
	elif compound_type == 'salt':
		df = S.salt
	else:
		raise ValueError('Compound type must be one of ["acid", "oxide", "salt", "all"]
		
	out = df.query_target(target_element)['Formula'].tolist()
	return out

#get_compound_list(select_target_element.value, select_compound_type.value)

def get_mass_frac(mass_frac):
	return mass_frac
	
select_mass_frac=widgets.BoundedFloatText(description='Mass Fraction:', width=75, min=0, max=1)

#get_mass_frac(select_mass_frac)

def get_mass_frac_min(mass_frac_min):
	return mass_frac_min
	
select_mass_frac_min = widgets.BoundedFloatText(description='Min:', width=75,min=0,max=1)

#get_mass_frac_min(select_mass_frac_min)

def get_mass_frac_max(mass_frac_max):
	return mass_frac_max
	
select_mass_frac_max = widgets.BoundedFloatText(description='Max:',width=75,min=0,max=1)

#get_mass_frac_max(select_mass_frac_max)

class 
