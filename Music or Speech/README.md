* zcr_rms.py finds the percentage of low energy frames in a sound file and the mean of the variance of zero crossing rates (ZCRs) for each second.
* zcr_fin.py finds the mean and variance of the RMS values as well.

The approach is based on [this paper](http://www.ee.columbia.edu/~dpwe/classes/e4810-2013-09/projects/cvcotton.pdf) by Courtenay Cotton, Columbia University.

Results we obtained:

### Music files:

| Filename | Percentage of low energy frames | Mean of variance of ZCR | Mean of RMS values | Variance of RMS values |
| :------: | :-----------------------------: | :---------------------: | :----------------: | :--------------------: |
| hello2   |  1.608%                         | 217.562                 | 3754.354           | 4400.447               |
| six-sec_fire | 8.870%                      | 191.854                 | 3739.978           | 4353.832               |
| six-sec_paradise | 0.0%                    | 215.462                 | 3705.166           | 4292.080               |
| six-sec_paradise2 | 0.0%                   | 227.284                 | 3736.195           | 4631.577               |
| stairway2         | 0.585%                 | 220.826                 | 3725.040           | 4549.494               |
| stairway3         | 0.0%                   | 213.793                 | 3736.531           | 4033.603               |
| stairway4         | 0.0%                   | 213.175                 | 3736.919           | 4379.937               |
| six-sec_wonderwall | 0.0%                  | 330.768                 | 3695.484           | 4992.895               |
| hello3             | 4.0%                  | 463.651                 | 3708.044           | 7503.268               |


### Speech files:

| Filename | Percentage of low energy frames | Mean of variance of ZCR | Mean of RMS values | Variance of RMS values |
| :------: | :-----------------------------: | :---------------------: | :----------------: | :--------------------: |
| six-sec_michelle | 49.603%                 | 5439.593                | 2936.190           | 1033288.506            |
| six-sec_jkrowling | 40.239%                | 12466.890               | 2730.110           | 1067895.238            |
| six-sec_kalam | 25.6%                      | 2141.229                | 3619.399           | 238881.303             |
| six-sec_amitabh | 38.8%                    | 448.425                 | 3711.828           | 8928.889               |
| six-sec_steve   | 30.243%                  | 2213.244                | 3627.163           | 36218.872              |
| six-sec_srinda  | 48.0%                    | 4200.099                | 3621.816           | 28548.794              |
| six-sec_geoffrey | 36.290%                 | 1516.970                | 3599.546           | 299034.856             |