###########################################
##  Day 6: 30 Days of python programming  #
###########################################

# Exercises: Level 1

# 1 - Create an empty tuple
new_tpl = ()
print(type(new_tpl))

# 2 - Create a tuple containing names of your sisters and your brothers (imaginary siblings are fine)
tpl_sister = ('Erin', 'Samantha', 'Corine', 'Karine', 'Elisabeth')
tpl_brother = ('Marc', 'Christophe', 'Eric', 'Jordan')
print(tpl_sister)
print(tpl_sister)

# 3 - Join brothers and sisters tuples and assign it to siblings
tpl_siblings = tpl_brother + tpl_sister
print(tpl_siblings)

# 4 - How many siblings do you have?
print(len(tpl_siblings))

# 5 - Modify the siblings tuple and add the name of your father and mother and assign it to family_members
family_members = tpl_siblings + ('André', 'Geneviève')
print(family_members)
