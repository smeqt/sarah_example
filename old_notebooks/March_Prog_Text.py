import pandas


df_oxides = pandas.read_csv('./data/oxide.cvs')
df_salts = pandas.read_csv('./data/salt.csv')

unique_elements_oxides = df_oxides.Target.unique()
unique_elements_salts = df_salts.Target.unique()


def get_element(element):
        """
        Create function that prompts user to input target element

        Parameters
        ----------

        element: str

        entered through widget (Select)
        """
	return element
	


select_target_element = widgets.Select(
	options=[element_list],height=60,width=50)
	
#get_element(select_target_element)

def get_compound_type(compound_type):
	return df_compound_type
	#???

select_compound_type = widgets.Dropdown(
	options = ['Acids', 'Oxides', 'Salts'],
	value = '',
	description = 'Type of Compound: '
)

#get_compound_type(select_compound_type)

# df_oxides = pd.read_csv('./data/oxide.csv')
# df_salts = pd.read_csv('./data/salt.csv')

# unique_elements_oxides = df_oxides.Target.unique()
# unique_elements_salts = df_salts.Target.unique()

def get_compound(df, compound):
	return df[df['Compound']==element.Formula.unique()]

#get_compound(select_compound_type,select_target_element)

def get_mass_frac(mass_frac):
	return mass_frac
	
select_mass_frac = widgets.BoundedFloatText(description='Mass Fraction:', width=75, min=0, max=1)

#get_mass_frac(select_mass_frac)

def get_mass_frac_min(mass_frac_min):
	return mass_frac_min
	
select_mass_frac_min = widgets.BoundedFloatText(description='Min:', width=75,min=0,max=1)

#get_mass_frac_min(select_mass_frac_min)

def get_mass_frac_max(mass_frac_max):
	return mass_frac_max
	
select_mass_frac_max = widgets.BoundedFloatText(description='Max:',width=75,min=0,max=1)

#get_mass_frac_max(select_mass_frac_max)


