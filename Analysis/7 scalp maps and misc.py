



#### Load Libraries
import mne
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable, axes_size
import pandas as pd
import numpy as np


############################################# check number of trials
sub_num = ['02','03','04','05','06','07','09','10','11','12',
           '13','14','15','17','20']
patho = 'S:/expt/eeg/eeg01/data/eeglab_NEW'
cond_new = []
cond_o1 = []
cond_o2 = []
cond_o3 = []
for x in sub_num: #loop through subjects
    #get path for data
    path = '%s/eeg01_sub%s_mcrsbpe_ica_eyerej_epochrej_ica2_manrej_chaninterp.set'%(patho,x)
    #load data
    dat = mne.io.read_epochs_eeglab(path)
    dat2 = dat.get_data()
    epoch_length = dat2.shape[0]
    #(trials, electrodes, time)
    path2 = 'S:/expt/eeg/eeg01/analyses/subject_data_files/eeg01_sub%s_trial_data_temp.csv'%(x)
    trialdat = pd.read_csv(path2)
    trialdat['unique_position'] = list(range(0,len(trialdat)))
    trialdat_include = trialdat[trialdat['eeg_rejected']==0] #exclude rejected trials
    trialdat_include['unique_id'] = list(range(0,len(trialdat_include)))    
    #### for repetitions, we want to keep event_types of 1,2,3,4
    cond_new = np.append(cond_new,
                         len(np.where(trialdat_include.event_type == 1)[0]))
    cond_o1 = np.append(cond_o1,
                        len(np.where(trialdat_include.event_type == 2)[0]))
    cond_o2 = np.append(cond_o2,
                        len(np.where(trialdat_include.event_type == 3)[0]))
    cond_o3 = np.append(cond_o3,
                        len(np.where(trialdat_include.event_type == 4)[0]))
print(np.round(np.mean(cond_new),decimals=2), '-',
      np.min(cond_new), '-',
      np.max(cond_new))
print(np.round(np.mean(cond_o1),decimals=2), '-',
      np.min(cond_o1), '-',
      np.max(cond_o1))
print(np.round(np.mean(cond_o2),decimals=2), '-',
      np.min(cond_o2), '-',
      np.max(cond_o2))
print(np.round(np.mean(cond_o3),decimals=2), '-',
      np.min(cond_o3), '-',
      np.max(cond_o3))

############################################# blank scalp map
path = 'S:/expt/eeg/eeg01/data/eeglab_NEW/eeg01_sub02_mcrsbpe_ica_eyerej_epochrej_ica2_manrej_chaninterp.set'
dat = mne.io.read_epochs_eeglab(path)
#### Plot Topo Maps
montage = mne.channels.read_montage('standard_1005')
poss = pd.DataFrame(montage.get_pos2d())
poss['name'] = montage.ch_names
poss2 = poss.loc[poss['name'].isin(dat.ch_names)]
fig, ax_topo = plt.subplots(1, 1, figsize=(5, 5), dpi=200)
gs1 = gridspec.GridSpec(13,5)
gs1.update(wspace=0.00025) # set the spacing between axes.
aspect = 20
pad_fraction = 0.5
im0, _ = mne.viz.plot_topomap(pd.Series(np.repeat(0,59)),
                              poss2.iloc[:,0:2].values,
                     contours=1, cmap = 'Greys',
                     vmin=0, vmax=np.max, axes=ax_topo, show=False)
plt.show()



############################################ scalp maps
#### Load Data
sub_num = ['02','03','04','05','06','07','09','10','11','12',
           '13','14','15','17','20']
eegNEW_list = list()
eegO1_list = list()
eegO2_list = list()
eegO3_list = list()

for x in sub_num: #loop through subjects
    #get path for data
    path = 'S:/expt/eeg/eeg01/data/eeglab_NEW/eeg01_sub%s_mcrsbpe_ica_eyerej_epochrej_ica2_manrej_chaninterp.set'%(x)
    #load data
    dat = mne.io.read_epochs_eeglab(path)
    dat2 = dat.get_data()
    epoch_length = dat2.shape[0]
    #(trials, electrodes, time)
    path2 = 'S:/expt/eeg/eeg01/analyses/subject_data_files/eeg01_sub%s_trial_data_temp.csv'%(x)
    trialdat = pd.read_csv(path2)
    trialdat['unique_position'] = list(range(0,len(trialdat)))
    trialdat_include = trialdat[trialdat['eeg_rejected']==0] #exclude rejected trials
    trialdat_include['unique_id'] = list(range(0,len(trialdat_include)))
    # baseline individual trials
    for trialz in list(range(0,dat2.shape[0])):
        base_avgs = dat2[0,:,0:100].mean(axis=1)
        for elecx in list(range(0,59)):
            dat2[trialz, elecx, :] = dat2[trialz, elecx, :] - base_avgs[elecx]
    # for repetitions, we want to keep event_types of 1,2,3,4
    where1 = np.where(trialdat_include.event_type == 1)[0]
    where2 = np.where(trialdat_include.event_type == 2)[0]
    where3 = np.where(trialdat_include.event_type == 3)[0]
    where4 = np.where(trialdat_include.event_type == 4)[0]
    eegNEW_list.append(np.average(dat2[where1,:,:], axis=0))
    eegO1_list.append(np.average(dat2[where2,:,:], axis=0))
    eegO2_list.append(np.average(dat2[where3,:,:], axis=0))
    eegO3_list.append(np.average(dat2[where4,:,:], axis=0))
    print(x)
    

#### Average ERPs
Enew = (sum(eegNEW_list) / len(eegNEW_list)) * 1e6
Eo1 = pd.DataFrame(((sum(eegO1_list) / len(eegO1_list)) * 1e6) - Enew)
Eo2 = pd.DataFrame(((sum(eegO2_list) / len(eegO2_list)) * 1e6) - Enew)
Eo3 = pd.DataFrame(((sum(eegO3_list) / len(eegO3_list)) * 1e6) - Enew)

sec_list = np.arange(-495, 1505, 5)
Eo1.columns = sec_list
Eo2.columns = sec_list
Eo3.columns = sec_list

Eo1x = Eo1.loc[:,500:800].mean(axis=1)
Eo2x = Eo2.loc[:,500:800].mean(axis=1)
Eo3x = Eo3.loc[:,500:800].mean(axis=1)

#### Plot Topo Maps
montage = mne.channels.read_montage('standard_1005')
poss = pd.DataFrame(montage.get_pos2d())
poss['name'] = montage.ch_names
poss2 = poss.loc[poss['name'].isin(dat.ch_names)]

plt.rcParams["font.family"] = "Arial"
fig, ax_topo = plt.subplots(1, 3, figsize=(13, 5), dpi=100)
gs1 = gridspec.GridSpec(13,5)
gs1.update(wspace=0.00025) # set the spacing between axes.
aspect = 20
pad_fraction = 0.5
im0, _ = mne.viz.plot_topomap(Eo1x, poss2.iloc[:,0:2].values,
                     contours=0, cmap = 'YlOrRd',
                     vmin=np.min, vmax=np.max, axes=ax_topo[0], show=False)
ax_topo[0].set_title('Old 1 - New', size = 25)
im1, _ = mne.viz.plot_topomap(Eo2x, poss2.iloc[:,0:2].values,
                     contours=0,cmap = 'YlOrRd',
                     vmin=np.min, vmax=np.max, axes=ax_topo[1], show=False)
ax_topo[1].set_title('Old 2 - New', size = 25)
im2, _ = mne.viz.plot_topomap(Eo3x, poss2.iloc[:,0:2].values,
                     contours=0,cmap = 'YlOrRd',
                     vmin=np.min, vmax=np.max, axes=ax_topo[2], show=False)
divider = make_axes_locatable(ax_topo[2])
width = axes_size.AxesY(ax_topo[2], aspect=1./aspect)
pad = axes_size.Fraction(pad_fraction, width)
ax_colorbar = divider.append_axes('right', size=width, pad=pad)
cbar = plt.colorbar(im0,cax=ax_colorbar)
cbar.ax.tick_params(labelsize=18, direction = 'in')
cbar.set_label(u'\u03bc V', size = 20)
ax_topo[2].set_title('Old 3 - New', size = 25)
plt.show()

#### without colorbar to make maps even size
plt.rcParams["font.family"] = "Arial"
fig, ax_topo = plt.subplots(1, 3, figsize=(13, 5),dpi=100)
gs1 = gridspec.GridSpec(13,5)
gs1.update(wspace=0.00025) # set the spacing between axes.
im0, _ = mne.viz.plot_topomap(Eo1x, poss2.iloc[:,0:2].values,
                     contours=0, cmap = 'YlOrRd',
                     vmin=np.min, vmax=np.max, axes=ax_topo[0], show=False)
ax_topo[0].set_title('Old 1 - New', size = 25)
im1, _ = mne.viz.plot_topomap(Eo2x, poss2.iloc[:,0:2].values,
                     contours=0,cmap = 'YlOrRd',
                     vmin=np.min, vmax=np.max, axes=ax_topo[1], show=False)
ax_topo[1].set_title('Old 2 - New', size = 25)
im2, _ = mne.viz.plot_topomap(Eo3x, poss2.iloc[:,0:2].values,
                     contours=0,cmap = 'YlOrRd',
                     vmin=np.min, vmax=np.max, axes=ax_topo[2], show=False)
ax_topo[2].set_title('Old 3 - New', size = 25)
plt.show()


