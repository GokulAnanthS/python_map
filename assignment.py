import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
# reading the CSV fie
df = pd.read_csv("GrowLocations.csv")

# Cleaning dataset

# Renaming the CSV
df = df.rename(columns={'Latitude': 'Longitude', 'Longitude': 'Latitude'})
# Remove NA
df = df.dropna()
bounding_box = {
    'min_lon': -10.592,
    'max_lon': 1.6848,
    'min_lat': 50.681,
    'max_lat': 57.985
}
df = df[(df['Longitude'] >= bounding_box['min_lon']) & (df['Longitude'] <= bounding_box['max_lon']) &
         (df['Latitude'] >= bounding_box['min_lat']) & (df['Latitude'] <= bounding_box['max_lat'])]

image_path = 'map7.png'
uk_map_img = mpimg.imread(image_path)
# Create a scatter plot with color mapping
fig, ax = plt.subplots(figsize=(10, 6))

ax.scatter(df["Longitude"], df["Latitude"], color="fuchsia")
ax.imshow(uk_map_img, extent=(-10.592, 1.6848, 50.681, 57.985))
# Set labels and title
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Plotting the GROW data')
# Show the plot
plt.show()