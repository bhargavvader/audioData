* zcr_rms.py finds the percentage of low energy frames in a sound file and the mean of the variance of zero crossing rates (ZCRs) for each second.
* zcr_fin.py finds the mean and variance of the RMS values as well.

The approach is based on [this paper](http://www.ee.columbia.edu/~dpwe/classes/e4810-2013-09/projects/cvcotton.pdf) by Courtenay Cotton, Columbia University.

Results we obtained:

### Music files:

| Filename | Percentage of low energy frames | Mean of variance of ZCR | Mean of RMS values | Variance of RMS values |
| :------: | :-----------------------------: | :---------------------: | :----------------: | :--------------------: |
| hello2   |  1.608%                         | 217.562                 | 3754.354           | 4400.447               |
| six-sec_fire | 8.870%                      | 191.854                 | 3739.978           | 4353.832               |
| six-sec_paradise | 0.0%                    | 215.462                 | | |
| six-sec_paradise2 | 0.0%                   | 227.284                 | | |
| stairway2         | 0.585%                 | 220.826                 | | |
| stairway3         | 0.0%                   | 213.793                 | | |
| stairway4         | 0.0%                   | 213.175                 | | |
| six-sec_wonderwall | 0.0%                  | 330.768                 | | |
| hello3             | 4.0%                  | 463.651                 | | |


### Speech files:

| Filename | Percentage of low energy frames | Mean of variance of ZCR |
| :------: | :-----------------------------: | :---------------------: |
| six-sec_michelle | 49.603%                 | 5439.593                |
| six-sec_jkrowling | 40.239%                | 12466.890               |
| six-sec_kalam | 25.6%                      | 2141.229                |
| six-sec_amitabh | 38.8%                    | 448.425                 |