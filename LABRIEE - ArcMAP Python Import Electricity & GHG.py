#Call Libraries
import arcpy
from arcpy import env

#Note on units
#Elec := Electricity consumption per year (kWh)
#GHGel := GHG emissions from electricity per year (kg CO2e)

#Create new fields with the names that we want
arcpy.AddField_management("LADWP_EN","Plus4","TEXT","","","","Plus4","NULLABLE","NON_REQUIRED","")
arcpy.AddField_management("LADWP_EN","ZipPlus4","TEXT","","a,"","ZipPlus4","NULLABLE","NON_REQUIRED","")
arcpy.AddField_management("LADWP_EN","PostlCode","TEXT","","","","PostlCode","NULLABLE","NON_REQUIRED","")
for i in range(6): 
	arcpy.AddField_management("LADWP_EN","Elec%s" %(i+2005),"DOUBLE","","","","Elec%s" %(i+2005),"NULLABLE","NON_REQUIRED","")
	arcpy.AddField_management("LADWP_EN","GHGel%s" %(i+2005),"DOUBLE","","","","GHGel%s" %(i+2005),"NULLABLE","NON_REQUIRED","")
 
##Assign values to new field names
#Zip index values (Text)
arcpy.CalculateField_management("LADWP_EN","Plus4","[X4]","VB","")
arcpy.CalculateField_management("LADWP_EN","ZipPlus4","[ZIP___4]","VB","")
arcpy.CalculateField_management("LADWP_EN","PostlCode","[ACCOUNT_PO]","VB","")

#Electricity consumption (kWh)
arcpy.CalculateField_management("LADWP_EN","Elec2005","[X005]","VB","")
arcpy.CalculateField_management("LADWP_EN","Elec2006","[X006]","VB","")
arcpy.CalculateField_management("LADWP_EN","Elec2007","[X007]","VB","")
arcpy.CalculateField_management("LADWP_EN","Elec2008","[X008]","VB","")
arcpy.CalculateField_management("LADWP_EN","Elec2009","[ELEC_2009]","VB","")
arcpy.CalculateField_management("LADWP_EN","Elec2010","[ELEC_2010]","VB","")

#GHG emissions (kg CO2e); factors for electricity are hard coded in the same lines as calculations
arcpy.CalculateField_management("LADWP_EN","GHGel2005","[X005]*0.62","VB","")
arcpy.CalculateField_management("LADWP_EN","GHGel2006","[X006]*0.59","VB","")
arcpy.CalculateField_management("LADWP_EN","GHGel2007","[X007]*0.56","VB","")
arcpy.CalculateField_management("LADWP_EN","GHGel2008","[X008]*0.58","VB","")
arcpy.CalculateField_management("LADWP_EN","GHGel2009","[ELEC_2009]*0.48","VB","")
arcpy.CalculateField_management("LADWP_EN","GHGel2010","[ELEC_2010]*0.45","VB","")

#Delete unwanted fields
arcpy.DeleteField_management("LADWP_EN",["X4","ZIP___4","ACCOUNT_PO","X005","X006","X007","X008","ELEC_2009","ELEC_2010"])

#WARNING WARNING WARNING WARNING WARNING WARNING WARNING WARNING
#Temp - Delete new fields
arcpy.DeleteField_management("LADWP_EN",["Plus4","ZipPlus4","PostlCode"])
for i in range(6): 
	arcpy.DeleteField_management("LADWP_EN",["Elec%s" %(i+2005),"GHGel%s" %(i+2005)])
##################################################################
