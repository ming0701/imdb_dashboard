# imdb_dashboard

## Dashboard description

Our dashboard consists of one web page that shows 4 main reactive plots:

- The top rated movies by genre

This is a bar chart showing the genres on the x-axis and some kind of aggregation (e.g. count or average rating) on the y-axis. Each of the individual bars is also coloured by genre.

- How movie ratings vary over time

This is a line chart showing the years on the x-axis and the mean rating per genre on the y-axis. The individual lines may be coloured by other features such as genre or region of production.

- The top rated movies by actor

This is a bubble graph showing the mean rating on the y-axis and the year on the x-axis. Each bubble represents an actor and the size of the bubble represents the number of movies that that actor performed in. The user can choose the number of actors that are depicted for each year using a slider.

- A map showing summary statistics about movies produced in each region

Our dataset contains information from various regions around the world, so this map can be used to explore how movie characteristics vary by region. The map will show an aggregation for the movies produced in a particular region (e.g. the mean rating, the count, or mean number of ratings).

Additionally, we include a set of filters in a navigation pane on the left-hand side which allows used to filter the dataset by year, by actors, by genres, or by location. Changing these filters will update the data that is used to generate the plots. The displayed charts will be interactive enabling users to get more granular information by hovering over a point in a scatterplot or a bar in a bar graph.

## App sketch

## Contributions

|  Contributor  |  Github Username |
|--------------|------------------|
|  Abdul Moid Mohammed |  @iamMoid |
|  Brandon Lam |  @ming0701  |
|  Nikita Shymberg  |  @NikitaShymberg |

We welcome and recognize all contributions. Please find the guide for contribution in [Contributing Document](https://github.com/UBC-MDS/imdb_dashboard/blob/main/CONTRIBUTING.md).

## License

`imdb_dashboard` was created by Abdul Moid Mohammed, Brandon Lam and Nikita Shymberg. It is licensed under the terms of the MIT license.