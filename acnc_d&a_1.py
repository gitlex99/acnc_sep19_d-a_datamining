"""
Program: data preprocessing
Processes:
            * Normalise organisation attributes for python analysis.
            * Normalise organisation attributes/identifiers for Rattle/R analysis.
            * Potential scope for integration if another dataset that has an ABN attribute.
            * Data logging (hopefully done with a menu-report-making functionality).
Input: Data.gov ACNC September 2020 data.
Output: normalised/clean data (file) for further analysis.
Expected output: evidence-based and actionable actions/insights in regards to what high-performing (in regards to scale and outreach) in the charity environment.
                 Undestand if certain charity sectors/competitors/individual organisations/traits improve funding models (scale: small, medium, large).
"""
import matplotlib.pyplot as plt

#TODO: By Lex Bustillo. Last updated: 07/10/2020
acncRaw=open("datadotgov_main.txt")
# Holds >57,000 records of organisations, size, address, region(s) of operation and type of charity work.
# Columns: 62. Rows > 57,000.

#Source: https://data.gov.au/dataset/ds-dga-b050b242-4487-4306-abf5-07ca073e5594/distribution/dist-dga-eb1e6be4-5b13-4feb-b28e-388bf7c26f93/details?q=
# Data last updated: 28/09/2020

#TODO Intended output of program: DATA EXPLORATION - to identify potential correlation(s) with region or area of work with scale.

# Initialising key lists for dictionaries.
# Data headings (tab separated):
headerRaw="ABN	Charity_Legal_Name	Other_Organisation_Names	Address_Type	Address_Line_1	Address_Line_2	Address_Line_3	Town_City	State	Postcode	Country	Charity_Website	Registration_Date	Date_Organisation_Established	Charity_Size	Number_of_Responsible_Persons	Financial_Year_End	Operates_in_ACT	Operates_in_NSW	Operates_in_NT	Operates_in_QLD	Operates_in_SA	Operates_in_TAS	Operates_in_VIC	Operates_in_WA	Operating_Countries	PBI	HPC	Preventing_or_relieving_suffering_of_animals	Advancing_Culture	Advancing_Education	Advancing_Health	Promote_or_oppose_a_change_to_law__government_poll_or_prac	Advancing_natual_environment	Promoting_or_protecting_human_rights	Purposes_beneficial_to_ther_general_public_and_other_analogous	Promoting_reconciliation__mutual_respect_and_tolerance	Advancing_Religion	Advancing_social_or_public_welfare	Advancing_security_or_safety_of_Australia_or_Australian_public	Aboriginal_or_TSI	Adults	Aged_Persons	Children	Communities_Overseas	Early_Childhood	Ethnic_Groups	Families	Females	Financially_Disadvantaged	Gay_Lesbian_Bisexual	General_Community_in_Australia	Males	Migrants_Refugees_or_Asylum_Seekers	Other_Beneficiaries	Other_Charities	People_at_risk_of_homelessness	People_with_Chronic_Illness	People_with_Disabilities	Pre_Post_Release_Offenders	Rural_Regional_Remote_Communities	Unemployed_Person"

#Columns and 2-letter string codes for analysis, this is done since charities can perform activities in multiple areas (columns).
#This is done so that the program will create a FINGERPRINT for analysis (simplify analysis by avoid indexation boolean format ).
#          i.e. a FINGERPRINT of a large Charity that is Advancing Education & Health is formatted as: ScaleTypecode_Typcode_Typecode... ==> 3AE_AH_.
#          i.e. a FINGERPRINT of a small Charity to preven animal suffering, advance natural environment and oppose change of law ==> 1RA_NE_CL_
charityTypeCode1="RA_" # Preventing_or_relieving_suffering_of_animals
charityTypeCode2="AC_" # Advancing_Culture
charityTypeCode3="AE_" # Advancing_Education
charityTypeCode4="AH_" # Advancing_Health
charityTypeCode5="CL_" # Promote_or_oppose_a_change_to_law__government_poll_or_prac
charityTypeCode6="NE_" # Advancing_natual_environment
charityTypeCode7="HR_" # Promoting_or_protecting_human_rights
charityTypeCode8="GP_" # Purposes_beneficial_to_ther_general_public_and_other_analogous
charityTypeCode9="RC_" # Promoting_reconciliation__mutual_respect_and_tolerance
charityTypeCode10="AR_" # Advancing_Religion
charityTypeCode11="PW_" # Advancing_social_or_public_welfare
charityTypeCode12="SC_" # Advancing_security_or_safety_of_Australia_or_Australian_public
charityTypeCode13="AT_" # Aboriginal_or_TSI
charityTypeCode14="AD_" # Adults
charityTypeCode15="AP_" # Aged_Persons
charityTypeCode16="CH_" # Children
charityTypeCode17="CO_" # Communities_Overseas
charityTypeCode18="EC_" # Early_Childhood
charityTypeCode19="EG_" # Ethnic_Groups
charityTypeCode20="FL_" # Families
charityTypeCode21="FE_" # Females
charityTypeCode22="FD_" # Financially_Disadvantaged
charityTypeCode23="GL_" # Gay_Lesbian_Bisexual
charityTypeCode24="GC_" # General_Community_in_Australia
charityTypeCode25="MA_" # Males
charityTypeCode26="MR_" # Migrants_Refugees_or_Asylum_Seekers
charityTypeCode27="OB_" # Other_Beneficiaries
charityTypeCode28="OC_" # Other_Charities
charityTypeCode29="HM_" # People_at_risk_of_homelessness
charityTypeCode30="CR_" # People_with_Chronic_Illness
charityTypeCode31="DS_" # People_with_Disabilities
charityTypeCode32="OF_" # Pre_Post_Release_Offenders
charityTypeCode33="RR_" # Rural_Regional_Remote_Communities
charityTypeCode34="UN_" # Unemployed_Person


organisationListNames=[]
headersIndexDictionary={}
charityTypeDictionary={}

#To parse headers to help understand indexation of given data set (dictionaries).
headersParse1=headerRaw.split("\t")

headerCounter=0
for header in headersParse1:
    #headersParse2=("{} {},").format(header, headerCounter)
    #headersIndexDictionary[header]=headerCounter
    headersIndexDictionary[headerCounter] = header
    headerCounter+=1
# For Testing Purposes
# print(headersIndexDictionary)
# print(headersIndexDictionary[7])
# print(len(headersIndexDictionary))

# For Testing Purposes
# for h in range(len(headersIndexDictionary)):
#     #print("column: {} - {}".format(h,headersIndexDictionary[h]))
#     print(headersIndexDictionary[h])


# The text file is tab separated, this will split each line in that text into tabs to allow appending of elements.
for record in acncRaw:
    recordParse1=record.split("\t")
    organisationListNames.append(recordParse1[1])

# For Testing Purposes
#print(organisationListNames)
#print(len(organisationListNames))

acncRaw.close()

# ----------------------------------------------------------------------------------------------------------------------
menuStr="Source: ACNC Charities Register - Updated September 2020\n(1)Analysis by charity type\n(2)Analysis by charity size\n(3)Analysis by charity location(s)\n(4)Debug\n(x)Exit program\nPlease enter: "

uInput=input(menuStr)

def menu():
    userInput=input(menuStr)
    print(menuStr)
    if userInput=="1":
        print("1")
        #TODO perform method call for this analysis
    elif userInput=="2":
        print("2")
        # TODO perform method call for this analysis
    elif userInput=="3":
        print("3")
        # TODO perform method call for this analysis
    elif userInput=="4":
        print("4")
        # TODO perform method call for this analysis
    else:
        print("Please try again.")

while uInput!="x":
    menu()
