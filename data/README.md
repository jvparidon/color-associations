# Data files and contents

| Filename | Data |
|---|---|
| saysani_data.tsv | Color/adjective semantic differential ratings from the original Saysani experiment |
| replication1_data.csv | Color/adjective semantic differential ratings from the 1st replication study (sighted participants only) |
| replication2_data_with_reading.csv | Color/adjective semantic differential ratings from the 2nd replication study, includes reading measures (sighted participants only) |
| color_dimension_nameability.csv | Participant labels for color/adjective pairs, including modal response and number of responses |
| pair_labels_all.txt | Participant labels for color/adjective pairs, all labels |
| pair_labels_2plus.txt | Participant labels for color/adjective pairs, only labels with 2 or more mentions |
| viz_vs_ling_ratings.tsv | Participant ratings for linguistic vs. visual learnability of color/adjective relationships |
| data_plus_predictors.tsv | All color/adjective semantic differential ratings from the first three experiments, including covariates |

## Contents of viz_vs_ling_ratings.tsv
| Variable | Description |
|---|---|
| color | Color of the color/adjective pair to be rated, presented to participants in text form |
| adjective | Adjective of the color/adjective pair to be rated, presented to participants in text form |
| init_x | Initial X coordinate of moveable dot in pixels |
| init_y | Initial Y coordinate of moveable dot in pixels |
| final_x | Final X coordinate of moveable dot in pixels when trial was submitted |
| final_y | Final Y coordinate of moveable dot in pixels when trial was submitted |
| rt | Response time in milliseconds |
| index | trial number after randomization (meaningless because these data are averaged) |
| trial_num | trial number before randomization (meaningless because these data are averaged) |
| neither_vs_both | Final position of the moveable dot on the `neither` to `both` response axis |
| viz_vs_ling | Final position of the moveable dot on the `visual` to `linguistic` response axis |
| catch_score | Score on the catch trials (meaningless because these data are averaged) |