
import pandas as pd

def clean_csv_gt():
    col_names = [
    "Id", "ID_duplicated", "Child", "Adult", "Senior",
    "Female", "Male",
    "Upright", "Seated", "Recumbent",
    "Sedentary", "Moderate", "Vigorous",
    "Solitary", "Dyadic", "Group"
    ]

    # Leggi saltando la prima riga malformata
    gt_df = pd.read_csv("counts-analogico.csv", skiprows=1, header=None, names=col_names)

    # Rimuovi le colonne non necessarie
    gt_cleaned = gt_df.drop(columns=["ID_duplicated"])

    # Salva il file pulito
    gt_cleaned.to_csv("gt_cleaned.csv", index=False)

def clean_csv_modello():
    
    pred_df = pd.read_csv("counts-modello.csv")

    # Colonne da eliminare
    cols_to_drop = [
        "N individuals",
        "NEI Age",
        "NEI Sex",
        "NEI Bodily Posture",
        "NEI Activity Level",
        "NEI Social Configuration"
    ]

    # Rimozione colonne inutili
    pred_cleaned = pred_df.drop(columns=cols_to_drop)

    # Salvataggio dei risultati puliti
    pred_cleaned.to_csv("predictions.csv", index=False)    

if __name__ == "__main__":
    clean_csv_gt()
    clean_csv_modello()
