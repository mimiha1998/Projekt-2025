import pandas as pd
import os

def process_feature_file(input_file):
    # Lese die Excel-Datei
    df = pd.read_excel(input_file)
    
    # Erstelle neue Text-IDs
    text_types = ['en', 'es', 'de', 'esende', 'ende', 'esde']
    df['text_id'] = ''
    
    # Erstelle Text-IDs basierend auf der 'lang' Spalte
    for text_type in text_types:
        mask = df['lang'] == text_type
        df.loc[mask, 'text_id'] = [f"{text_type}{i+1}" for i in range(mask.sum())]
    
    # Entferne redundante Spalten wenn vorhanden
    if 'subcorp' in df.columns and df['subcorp'].equals(df['lang']):
        df = df.drop('subcorp', axis=1)
    
    # Sortiere die Spalten
    first_cols = ['text_id', 'doc', 'lang']
    other_cols = [col for col in df.columns if col not in first_cols]
    df = df[first_cols + other_cols]
    
    # Speichere die verarbeitete Datei
    output_file = os.path.splitext(input_file)[0] + '_processed.xlsx'
    df.to_excel(output_file, index=False)
    print(f"Verarbeitete Datei gespeichert als: {output_file}")
    
    # Zeige Zusammenfassung
    print("\nZusammenfassung:")
    print("Anzahl Dokumente pro Texttyp:")
    print(df['lang'].value_counts())
    print("\nBeispiel Text-IDs:")
    for text_type in text_types:
        if text_type in df['lang'].unique():
            print(f"\n{text_type}:")
            print(df[df['lang'] == text_type]['text_id'].head())

# Ausführen
if __name__ == "__main__":
    input_file = "C:/Users/Fox0197/Desktop/code/UD_features_en-es/get_feats/extraction/Data_neu.xlsx"  # Ändern Sie dies zu Ihrem Dateinamen
    process_feature_file(input_file)