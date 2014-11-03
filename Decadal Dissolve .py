#Call Libraries
import arcpy
from arcpy import env

#Run dissolve function
arcpy.Dissolve_management("EIrT1930"," E:\Daniel Burillo\LA Roads\Decadal Snapshots, Growth of LA Roads, Embedded E and GHG\Proceess Files\EIrTYYYY\EIrT1930_Dissolve.shp","CTIDFP00","SegLen_m SUM;T1500Len_m SUM;T1400Len_m SUM;T1300Len_m SUM;T1300Len_m SUM;T1200Len_m SUM;T1110Len_m SUM;RdArea_m2 SUM;AreaTr_m2 MEAN","MULTI_PART","DISSOLVE_LINES")


#Create new fields with the correct names that we want
arcpy.AddField_management("EIrT1930_Dissolve", "SegLen_m", "DOUBLE", "", "","","SegLen_m","NULLABLE","NON_REQUIRED","")

arcpy.AddField_management("EIrT1930_Dissolve", "T1500Len_m", "DOUBLE", "", "","","T1500Len_m","NULLABLE","NON_REQUIRED","")

arcpy.AddField_management("EIrT1930_Dissolve", "T1400Len_m", "DOUBLE", "", "","","T1400Len_m","NULLABLE","NON_REQUIRED","")

arcpy.AddField_management("EIrT1930_Dissolve", "T1300Len_m", "DOUBLE", "", "","","T1300Len_m","NULLABLE","NON_REQUIRED","")

arcpy.AddField_management("EIrT1930_Dissolve", "T1200Len_m", "DOUBLE", "", "","","T1200Len_m","NULLABLE","NON_REQUIRED","")

arcpy.AddField_management("EIrT1930_Dissolve", "T1110Len_m", "DOUBLE", "", "","","T1110Len_m","NULLABLE","NON_REQUIRED","")

arcpy.AddField_management("EIrT1930_Dissolve", "AreaRd_m2", "DOUBLE", "", "","","AreaRd_m2","NULLABLE","NON_REQUIRED","")

arcpy.AddField_management("EIrT1930_Dissolve", "AreaTr_m2", "DOUBLE", "", "","","AreaTr_m2","NULLABLE","NON_REQUIRED","")

#Calculate fields by copping over the values from the dissolve
arcpy.CalculateField_management("EIrT1930_Dissolve","SegLen_m","[SUM_SegLen]","VB","")

arcpy.CalculateField_management("EIrT1930_Dissolve","T1500Len_m","[SUM_T1500L]","VB","")

arcpy.CalculateField_management("EIrT1930_Dissolve","T1400Len_m","[SUM_T1400L]","VB","")

arcpy.CalculateField_management("EIrT1930_Dissolve","T1300Len_m","[SUM_T1300L]","VB","")

arcpy.CalculateField_management("EIrT1930_Dissolve","T1200Len_m","[SUM_T1200L]","VB","")

arcpy.CalculateField_management("EIrT1930_Dissolve","T1110Len_m","[SUM_T1110L]","VB","")

arcpy.CalculateField_management("EIrT1930_Dissolve","AreaRd_m2","[SUM_RdArea]","VB","")

arcpy.CalculateField_management("EIrT1930_Dissolve","AreaTr_m2","[MEAN_AreaT]","VB","")

	
#Delete the unwanted fields produced by the dissolve function
arcpy.DeleteField_management("EIrT1930_Dissolve",["SUM_SegLen","SUM_RdArea","SUM_T1110L","SUM_T1200L","SUM_T1300L","SUM_T130_1","SUM_T1400L","SUM_T1500L","MEAN_AreaT"])



#Join the Dissolve file to the Census Tracts with Area file
arcpy.DeleteField_management("EIrT1930_Dissolve",["SUM_SegLen","SUM_RdArea","SUM_T1110L","SUM_T1200L","SUM_T1300L","SUM_T130_1","SUM_T1400L","SUM_T1500L","MEAN_AreaT"])
