# Read data from the file and clean it
def cleanData():
    with open('./data/dawn.txt', 'r') as f:
        data = f.readlines()
        
        # Clean the data
        cleaned_data = []
        for line in data:
            cleaned_data.append(line.strip())
        
        # Write the cleaned data to a new file
        with open('./cleanedData/cleaned_dawn.txt', 'w') as f:
            for line in cleaned_data:
                f.write(line + '\n')

    with open('./data/bbc.txt', 'r') as f:
        data = f.readlines()
        
        # Clean the data
        cleaned_data = []
        for line in data:
            cleaned_data.append(line.strip())
        
        # Write the cleaned data to a new file
        with open('./cleanedData/cleaned_bbc.txt', 'w') as f:
            for line in cleaned_data:
                f.write(line + '\n')
        


cleanData()