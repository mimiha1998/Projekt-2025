import pandas as pd
import os

def convert_txt_to_excel():
    # Aktuelles Verzeichnis anzeigen
    current_dir = os.getcwd()
    print(f"Aktuelles Arbeitsverzeichnis: {current_dir}")
    
    # Input file
    input_file = 'output.txt'
    input_path = os.path.join(current_dir, input_file)
    print(f"\nSuche nach Input-Datei: {input_path}")
    
    if not os.path.exists(input_path):
        print(f"Fehler: {input_file} nicht gefunden!")
        return
    
    # Lese die TSV/TXT Datei
    print(f"\nLese {input_file}...")
    df = pd.read_csv(input_path, sep='\t')
    print(f"Gefundene Zeilen: {len(df)}")
    print(f"Gefundene Spalten: {len(df.columns)}")
    
    # Output file
    output_file = 'output_converted.xlsx'
    output_path = os.path.join(current_dir, output_file)
    print(f"\nSpeichere Excel-Datei als: {output_path}")
    
    # Speichere als Excel
    df.to_excel(output_path, index=False)
    print(f"Datei erfolgreich gespeichert!")
    
    return df

# Ausführen
if __name__ == "__main__":
    convert_txt_to_excel()