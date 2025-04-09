import pandas as pd
import numpy as np

if __name__ == "__main__":

    pred = pd.read_csv("predictions.csv")
    gt = pd.read_csv("gt_cleaned.csv")

    pred = pred.set_index("Id").sort_index()
    gt = gt.set_index("Id").sort_index()

    columns_to_compare = pred.columns

    mae = (pred[columns_to_compare] - gt[columns_to_compare]).abs().mean()
    print("Errore assoluto medio per categoria:\n", mae)

    # Calcolo del MAPE
    mape = {}
    for col in columns_to_compare:
        y_true = gt[col]
        y_pred = pred[col]

        # Evita la divisione per zero
        mask = y_true != 0
        if mask.sum() > 0:
            mape[col] = (np.abs((y_pred[mask] - y_true[mask]) / y_true[mask]) * 100).mean()
        else:
            mape[col] = np.nan  # Nessun dato valido per calcolare il MAPE

    print("MAPE (%) per categoria:\n")
    for k, v in mape.items():
        print(f"{k:<12}: {v:.2f}%" if not pd.isna(v) else f"{k:<12}: N/A (divisione per zero)")

    # Calcolo dell'errore assoluto per ogni immagine e categoria
    absolute_errors = (pred[columns_to_compare] - gt[columns_to_compare]).abs()

    # Calcolo errore massimo
    max_error = absolute_errors.max()

    # Calcolo deviazione standard (std)
    std_error = absolute_errors.std()

    print("Errore massimo per categoria:\n", max_error)
    print("\nDeviazione standard dell'errore per categoria:\n", std_error)

    category = "Sedentary"
    group_errors = (pred[category] - gt[category]).abs()
    top_group_errors = group_errors.sort_values(ascending=False).head(5)

    print(f"\nTop 5 errori assoluti per la categoria '{category}':\n", top_group_errors)

    category = "Moderate"
    group_errors = (pred[category] - gt[category]).abs()
    top_group_errors = group_errors.sort_values(ascending=False).head(5)

    print(f"\nTop 5 errori assoluti per la categoria '{category}':\n", top_group_errors)

    category = "Dyadic"
    group_errors = (pred[category] - gt[category]).abs()
    top_group_errors = group_errors.sort_values(ascending=False).head(5)

    print(f"\nTop 5 errori assoluti per la categoria '{category}':\n", top_group_errors)

    category = "Group"
    group_errors = (pred[category] - gt[category]).abs()
    top_group_errors = group_errors.sort_values(ascending=False).head(5)

    print(f"\nTop 5 errori assoluti per la categoria '{category}':\n", top_group_errors)