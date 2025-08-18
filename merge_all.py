def process_and_merge_data():
    # Lese beide Dateien
    df_old = pd.read_excel('Data_neu.xlsx')  # Die Datei von der Professorin
    df_new = pd.read_excel('output_converted.xlsx')  # Ihre konvertierte Datei
    
    # Kombiniere die Dataframes
    df_combined = pd.concat([df_old, df_new], ignore_index=True)
    
    # Erstelle neue Text-IDs
    text_types = ['en', 'es', 'esende', 'ende', 'esde']
    df_combined['text_id'] = ''
    
    for text_type in text_types:
        mask = df_combined['lang'] == text_type
        df_combined.loc[mask, 'text_id'] = [f"{text_type}{i+1}" 
                                          for i in range(mask.sum())]
    
    # Entferne redundante Spalte
    if 'subc' in df_combined.columns and df_combined['subc'].equals(df_combined['lang']):
        df_combined = df_combined.drop('subc', axis=1)
    
    # Speichere das Ergebnis
    df_combined.to_excel('combined_features.xlsx', index=False)
    return df_combined

# Kompletter Code als merge_all.py
import pandas as pd
import os

def merge_all_data():
    print("Starte Datenverarbeitung...")
    
    # 1. Konvertiere output.txt
    print("\nKonvertiere output.txt...")
    try:
        df_mega = pd.read_csv('output.txt', sep='\t')
        print(f"Gefundene Zeilen in output.txt: {len(df_mega)}")
    except Exception as e:
        print(f"Fehler beim Lesen von output.txt: {e}")
        return
    
    # 2. Lese alte Features
    print("\nLese alte Features...")
    try:
        df_old = pd.read_excel('Data_neu.xlsx')
        print(f"Gefundene Zeilen in alte_features.xlsx: {len(df_old)}")
    except Exception as e:
        print(f"Fehler beim Lesen der alten Features: {e}")
        return
    
    # 3. Kombiniere Daten
    print("\nKombiniere Daten...")
    df_combined = pd.concat([df_old, df_mega], ignore_index=True)
    
    # 4. Erstelle neue Text-IDs
    print("\nErstelle neue Text-IDs...")
    text_types = ['en', 'es', 'esende', 'ende', 'esde']
    df_combined['text_id'] = ''
    
    for text_type in text_types:
        mask = df_combined['lang'] == text_type
        count = mask.sum()
        if count > 0:
            df_combined.loc[mask, 'text_id'] = [f"{text_type}{i+1}" for i in range(count)]
            print(f"Erstellt: {count} IDs für {text_type}")
    
    # 5. Bereinige Spalten
    if 'subc' in df_combined.columns and df_combined['subc'].equals(df_combined['lang']):
        df_combined = df_combined.drop('subc', axis=1)
        print("\nRedundante 'subc' Spalte entfernt")
    
    # 6. Speichere Ergebnis
    output_file = 'combined_features.xlsx'
    df_combined.to_excel(output_file, index=False)
    print(f"\nErgebnis gespeichert in: {output_file}")
    print("\nZusammenfassung:")
    print(df_combined['lang'].value_counts())

if __name__ == "__main__":
    merge_all_data()