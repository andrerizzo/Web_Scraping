# Import necessary libraries
import requests
from bs4 import BeautifulSoup
import json
import os


def Extract_FP_and_Qualifying_Data(url, arquivo_json):
    # Header simulating a human request
    cabecalho = {"user-agent": "Mozilla/5.0"}

    # URL to be used
    url_name = url

    # Create an empty list
    pre_season_list = []

    # Request HTML file
    resposta = requests.get(url_name, cabecalho)

    # Parse HTML file
    html_text = BeautifulSoup(resposta.text, "html.parser")

    # Selecting table
    tabela = html_text.find("table")

    # Storing all rows into one variable
    for pre_season_data in tabela.find_all("tbody"):
        rows = pre_season_data.find_all("tr")

    # Looping through the HTML table to scrap data
    for row in rows:
        position = row.find_all("td")[0].text.strip()
        driver_number = row.find_all("td")[1].text.strip()
        driver_name = row.find_all("td")[2].text.strip()
        chassis = row.find_all("td")[4].text.strip()
        engine = row.find_all("td")[5].text.strip()
        laps = row.find_all("td")[6].text.strip()
        time = row.find_all("td")[7].text.strip()
        speed = row.find_all("td")[10].text.strip()

        pre_season_list.append({
            "Position": position,
            "Driver number": driver_number,
            "Driver name": driver_name,
            "Chassis": chassis,
            "Engine": engine,
            "Laps": laps,
            "Fastest lap": time,
            "Top speed": speed
        })

    # Importing array to a JSON file
    with open(arquivo_json, 'w') as json_file:
        json.dump(pre_season_list, json_file, indent=2)


def Extract_Grid_Data(url, arquivo_json):
    # Header simulating a human request
    cabecalho = {"user-agent": "Mozilla/5.0"}

    # URL to be used
    url_name = url

    # Create an empty list
    pre_season_list = []

    # Request HTML file
    resposta = requests.get(url_name, cabecalho)

    # Parse HTML file
    html_text = BeautifulSoup(resposta.text, "html.parser")

    # Selecting table
    tabela = html_text.find("table")

    # Storing all rows into one variable
    for pre_season_data in tabela.find_all("tbody"):
        rows = pre_season_data.find_all("tr")

    # Looping through the HTML table to scrap data
    for row in rows:
        position = row.find_all("td")[0].text.strip()
        driver_number = row.find_all("td")[1].text.strip()
        driver_name = row.find_all("td")[2].text.strip()
        chassis = row.find_all("td")[4].text.strip()
        engine = row.find_all("td")[5].text.strip()
        time = row.find_all("td")[6].text.strip()
        gap = row.find_all("td")[7].text.strip()
        speed = row.find_all("td")[8].text.strip()

        pre_season_list.append({
            "Position": position,
            "Driver number": driver_number,
            "Driver name": driver_name,
            "Chassis": chassis,
            "Engine": engine,
            "Time": time,
            "Gap": gap,
            "Speed": speed
        })

    # Importing array to a JSON file
    with open(arquivo_json, 'w') as json_file:
        json.dump(pre_season_list, json_file, indent=2)


def Extract_Racing_Data(url, arquivo_json):
    # Header simulating a human request
    cabecalho = {"user-agent": "Mozilla/5.0"}

    # URL to be used
    url_name = url

    # Create an empty list
    pre_season_list = []

    # Request HTML file
    resposta = requests.get(url_name, cabecalho)

    # Parse HTML file
    html_text = BeautifulSoup(resposta.text, "html.parser")

    # Selecting table
    tabela = html_text.find("table")

    # Storing all rows into one variable
    for pre_season_data in tabela.find_all("tbody"):
        rows = pre_season_data.find_all("tr")

    # Looping through the HTML table to scrap data
    for row in rows:
        position = row.find_all("td")[0].text.strip()
        driver_number = row.find_all("td")[1].text.strip()
        driver_name = row.find_all("td")[2].text.strip()
        chassis = row.find_all("td")[4].text.strip()
        engine = row.find_all("td")[5].text.strip()
        laps = row.find_all("td")[6].text.strip()
        time = row.find_all("td")[7].text.strip()
        gap = row.find_all("td")[8].text.strip()
        interval = row.find_all("td")[9].text.strip()
        pits = row.find_all("td")[11].text.strip()
        retirement = row.find_all("td")[12].text.strip()
        points = row.find_all("td")[13].text.strip()

        pre_season_list.append({
            "Position": position,
            "Driver number": driver_number,
            "Driver name": driver_name,
            "Chassis": chassis,
            "Engine": engine,
            "Laps": laps,
            "Time": time,
            "Gap": gap,
            "Interval": interval,
            "Pits": pits,
            "Retirement": retirement,
            "Points": points,
        })

    # Importing array to a JSON file
    with open(arquivo_json, 'w') as json_file:
        json.dump(pre_season_list, json_file, indent=2)


def Extract_Fastest_Laps_Data(url, arquivo_json):
    # Header simulating a human request
    cabecalho = {"user-agent": "Mozilla/5.0"}

    # URL to be used
    url_name = url

    # Create an empty list
    pre_season_list = []

    # Request HTML file
    resposta = requests.get(url_name, cabecalho)

    # Parse HTML file
    html_text = BeautifulSoup(resposta.text, "html.parser")

    # Selecting table
    tabela = html_text.find("table")

    # Storing all rows into one variable
    for pre_season_data in tabela.find_all("tbody"):
        rows = pre_season_data.find_all("tr")

    # Looping through the HTML table to scrap data
    for row in rows:
        position = row.find_all("td")[0].text.strip()
        driver_number = row.find_all("td")[1].text.strip()
        driver_name = row.find_all("td")[2].text.strip()
        chassis = row.find_all("td")[4].text.strip()
        engine = row.find_all("td")[5].text.strip()
        laps = row.find_all("td")[6].text.strip()
        time = row.find_all("td")[7].text.strip()
        gap = row.find_all("td")[8].text.strip()
        interval = row.find_all("td")[9].text.strip()
        speed = row.find_all("td")[10].text.strip()

        pre_season_list.append({
            "Position": position,
            "Driver number": driver_number,
            "Driver name": driver_name,
            "Chassis": chassis,
            "Engine": engine,
            "Laps": laps,
            "Time": time,
            "Gap": gap,
            "Interval": interval,
            "Speed": speed
        })

    # Importing array to a JSON file
    with open(arquivo_json, 'w') as json_file:
        json.dump(pre_season_list, json_file, indent=2)


def Tyre_Type_Full_Name(tyre_type_short_name):
    if (tyre_type_short_name == "S"):
        tyre_type_full_name = "Soft"
    elif (tyre_type_short_name == "M"):
        tyre_type_full_name = "Medium"
    elif (tyre_type_short_name == "H"):
        tyre_type_full_name = "Hard"
    elif (tyre_type_short_name == "I"):
        tyre_type_full_name = "Intermediary"
    elif (tyre_type_short_name == "W"):
        tyre_type_full_name = "Wet"
    else :
        tyre_type_full_name = "N/A"
    return tyre_type_full_name



def Extract_Tyre_History_Data(url, arquivo_json):
    # Header simulating a human request
    cabecalho = {"user-agent": "Mozilla/5.0"}

    # URL to be used
    url_name = url

    # Create an empty list
    pre_season_list = []

    # Request HTML file
    resposta = requests.get(url_name, cabecalho)

    # Parse HTML file
    html_text = BeautifulSoup(resposta.text, "html.parser")

    # Selecting table
    tabela = html_text.find("table")

    # Storing all rows into one variable
    for pre_season_data in tabela.find_all("tbody"):
        rows = pre_season_data.find_all("tr")

    # Looping through the HTML table to scrap data
    for row in rows:
        position = row.find_all("td")[0].text.strip()
        driver_number = row.find_all("td")[1].text.strip()
        driver_name = row.find_all("td")[2].text.strip()
        chassis = row.find_all("td")[4].text.strip()
        engine = row.find_all("td")[5].text.strip()
        PS1_tyre_type = Tyre_Type_Full_Name(row.find_all("td")[6].text.strip())
        PS1_lap = row.find_all("td")[7].text.strip()
        PS2_tyre_type = Tyre_Type_Full_Name(row.find_all("td")[8].text.strip())
        PS2_lap = row.find_all("td")[9].text.strip()
        PS3_tyre_type = Tyre_Type_Full_Name(row.find_all("td")[10].text.strip())
        PS3_lap = row.find_all("td")[11].text.strip()
        PS4_tyre_type = Tyre_Type_Full_Name(row.find_all("td")[12].text.strip())
        PS4_lap = row.find_all("td")[13].text.strip()
        PS5_tyre_type = Tyre_Type_Full_Name(row.find_all("td")[14].text.strip())
        PS5_lap = row.find_all("td")[15].text.strip()
        PS6_tyre_type = Tyre_Type_Full_Name(row.find_all("td")[16].text.strip())
        PS6_lap = row.find_all("td")[17].text.strip()
        PS7_tyre_type = Tyre_Type_Full_Name(row.find_all("td")[18].text.strip())
        PS7_lap = row.find_all("td")[19].text.strip()

        pre_season_list.append({
            "Position": position,
            "Driver number": driver_number,
            "Driver name": driver_name,
            "Chassis": chassis,
            "Engine": engine,
            "Pit stop 1 tyre type": PS1_tyre_type,
            "Pit stop 1 elapsed laps" : PS1_lap,
            "Pit stop 2 tyre type": PS2_tyre_type,
            "Pit stop 2 elapsed laps": PS2_lap,
            "Pit stop 3 tyre type": PS3_tyre_type,
            "Pit stop 3 elapsed laps": PS3_lap,
            "Pit stop 4 tyre type": PS4_tyre_type,
            "Pit stop 4 elapsed laps": PS4_lap,
            "Pit stop 5 tyre type": PS5_tyre_type,
            "Pit stop 5 elapsed laps": PS5_lap,
            "Pit stop 6 tyre type": PS6_tyre_type,
            "Pit stop 6 elapsed laps": PS6_lap,
            "Pit stop 7 tyre type": PS7_tyre_type,
            "Pit stop 7 elapsed laps": PS7_lap
        })

    # Importing array to a JSON file
    with open(arquivo_json, 'w') as json_file:
        json.dump(pre_season_list, json_file, indent=2)



# LOAD PRE-SEASON DATA

# # CREATE DIR
# # Directories
# directory = "F1_data"
# subdirectory_1 = "2023"
# subdirectory_2 = "Pre_Season"
#
# # Parent directory path
# parent_dir = "/home/admin/PycharmProjects/"
#
# # Path
# path = os.path.join(parent_dir, directory, subdirectory_1, subdirectory_2)
#
# # Create dir
# os.mkdir(path)


url = "https://www.motorsport.com/f1/results/2023/bahrain-february-testing/?st=Test+1"
arquivo_json = "Pre_Season_T1_2023"
Extract_FP_and_Qualifying_Data(url, arquivo_json)

url = "https://www.motorsport.com/f1/results/2023/bahrain-february-testing/?st=Test+2"
arquivo_json = "Pre_Season_T2_2023"
Extract_FP_and_Qualifying_Data(url, arquivo_json)

url = "https://www.motorsport.com/f1/results/2023/bahrain-february-testing/?st=Test+3"
arquivo_json = "Pre_Season_T3_2023"
Extract_FP_and_Qualifying_Data(url, arquivo_json)


# LOAD FREE PRACTICE AND QUALIFYING DATA - BAHRAIN

# CREATE DIR
# # Directories
# directory = "F1_data"
# subdirectory_1 = "2023"
# subdirectory_2 = "Season"
# subdirectory_3 = "01_Bahrain"
#
# # Parent directory path
# parent_dir = "/home/admin/PycharmProjects/"
#
# # Path
# path = os.path.join(parent_dir, directory, subdirectory_1, subdirectory_2, subdirectory_3)
#
# # Create dir
# os.mkdir(path)


# FP1
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=FP1"
    arquivo_json = "Bahrain_FP1_2023"
    Extract_FP_and_Qualifying_Data(url, arquivo_json)
    print("Free Practice 1 data loaded sucessfully.")
except:
    print("Error in Free Practice 1 data loading.")


# FP2
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=FP2"
    arquivo_json = "Bahrain_FP2_2023"
    Extract_FP_and_Qualifying_Data(url, arquivo_json)
    print("Free Practice 2 data loaded sucessfully.")
except:
    print("Error in Free Practice 2 data loading.")


# FP3
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=FP3"
    arquivo_json = "Bahrain_FP3_2023"
    Extract_FP_and_Qualifying_Data(url, arquivo_json)
    print("Free Practice 3 data loaded sucessfully.")
except:
    print("Error in Free Practice 3 data loading.")


# Q1
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=Q1"
    arquivo_json = "Bahrain_Q1_2023"
    Extract_FP_and_Qualifying_Data(url, arquivo_json)
    print("Q1 data loaded sucessfully.")
except:
    print("Error in Q1 data loading.")


# Q2
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=Q2"
    arquivo_json = "Bahrain_Q2_2023"
    Extract_FP_and_Qualifying_Data(url, arquivo_json)
    print("Q2 data loaded sucessfully.")
except:
    print("Error in Q2 data loading.")


# Q3
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=Q3"
    arquivo_json = "Bahrain_Q3_2023"
    Extract_FP_and_Qualifying_Data(url, arquivo_json)
    print("Q3 data loaded sucessfully.")
except:
    print("Error in Q3 data loading.")


# LOAD GRID DATA
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=GRID"
    arquivo_json = "Bahrain_Grid_2023"
    Extract_Grid_Data(url, arquivo_json)
    print("Grid data loaded sucessfully.")
except:
    print("Error in Grid data loading.")


# LOAD RACING DATA
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=RACE"
    arquivo_json = "Bahrain_Race_2023"
    Extract_Racing_Data(url, arquivo_json)
    print("Racing data loaded sucessfully.")
except:
    print("Error in Racing data loading.")


# FASTEST LAPS DATA
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=FL"
    arquivo_json = "Bahrain_GP_Fastest_Laps_2023"
    Extract_Fastest_Laps_Data(url, arquivo_json)
    print("Fastest laps data loaded sucessfully.")
except:
    print("Error in Fastest Laps data loading.")


# TYRE HISTORY DATA
try:
    url = "https://www.motorsport.com/f1/results/2023/bahrain-gp-625268/?st=TH"
    arquivo_json = "Bahrain_GP_Tyre_History_2023"
    Extract_Tyre_History_Data(url, arquivo_json)
    print("Tyre History data loaded sucessfully.")
except:
    print("Error in Tyre History data loading.")




