


library(readxl)
library(reshape2)
library(ggplot2)
library(cowplot)
library(tidyquant)
dat <- read_excel("S:/expt/eeg/eeg01/analyses/erps_conds_by9electrodes.csv", 
                  col_names = FALSE)

f3dat = dat[,c(1:4)]
colnames(f3dat) = c('New','Old1','Old2','Old3')
f3dat$time = seq(-500,1495,5)
fzdat = dat[,c(5:8)]
colnames(fzdat) = c('New','Old1','Old2','Old3')
fzdat$time = seq(-500,1495,5)
f4dat = dat[,c(9:12)]
colnames(f4dat) = c('New','Old1','Old2','Old3')
f4dat$time = seq(-500,1495,5)
c3dat = dat[,c(13:16)]
colnames(c3dat) = c('New','Old1','Old2','Old3')
c3dat$time = seq(-500,1495,5)
czdat = dat[,c(17:20)]
colnames(czdat) = c('New','Old1','Old2','Old3')
czdat$time = seq(-500,1495,5)
c4dat = dat[,c(21:24)]
colnames(c4dat) = c('New','Old1','Old2','Old3')
c4dat$time = seq(-500,1495,5)
p3dat = dat[,c(25:28)]
colnames(p3dat) = c('New','Old1','Old2','Old3')
p3dat$time = seq(-500,1495,5)
pzdat = dat[,c(29:32)]
colnames(pzdat) = c('New','Old1','Old2','Old3')
pzdat$time = seq(-500,1495,5)
p4dat = dat[,c(33:36)]
colnames(p4dat) = c('New','Old1','Old2','Old3')
p4dat$time = seq(-500,1495,5)


f3dat_long = melt(f3dat, id.vars = 'time')
fzdat_long = melt(fzdat, id.vars = 'time')
f4dat_long = melt(f4dat, id.vars = 'time')
c3dat_long = melt(c3dat, id.vars = 'time')
czdat_long = melt(czdat, id.vars = 'time')
c4dat_long = melt(c4dat, id.vars = 'time')
p3dat_long = melt(p3dat, id.vars = 'time')
pzdat_long = melt(pzdat, id.vars = 'time')
p4dat_long = melt(p4dat, id.vars = 'time')


theme = theme(panel.grid.major = element_blank(), 
              panel.grid.minor = element_blank(), 
              panel.background = element_blank(), 
              axis.line = element_line(colour = "black"), 
              legend.key = element_rect(fill = "white"),
              text = element_text(size = 29),
              legend.position='none',
              plot.title = element_text(size = 29, face = 'plain'),
              axis.text.x= element_text(size=24),
              axis.text.y= element_text(size=24))
theme2 = theme(panel.grid.major = element_blank(), 
               panel.grid.minor = element_blank(), 
               panel.background = element_blank(), 
               axis.line = element_line(colour = "black"), 
               legend.key = element_rect(fill = "white"),
               text = element_text(size = 29),
               #legend.position='none',
               plot.title = element_text(size = 29, face = 'plain'),
               axis.text.x= element_text(size=24),
               axis.text.y= element_text(size=24))

## Plot ERP
windowsFonts(Times=windowsFont("Arial"))

p1 = ggplot(f3dat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "",y = expression(paste("Amplitude (",mu,"V)")),colour = "")+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('F3')
p2 = ggplot(fzdat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "",y = '')+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('Fz')
p3 = ggplot(f4dat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "",y = '')+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('F4')
p4 = ggplot(c3dat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "",y = expression(paste("Amplitude (",mu,"V)")),colour = "")+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('C3')
p5 = ggplot(czdat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "",y = '')+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('Cz')
p6 = ggplot(c4dat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "",y = '')+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('C4')
p7 = ggplot(p3dat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "Time (ms)",y = expression(paste("Amplitude (",mu,"V)")),colour = "")+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('P3')
p8 = ggplot(pzdat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(values=c('black','red','darkgreen','blue'))+
  labs(x = "Time (ms)",y = '')+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme+
  coord_cartesian(ylim=c(-6,15)) + ggtitle('Pz')
p9 = ggplot(p4dat_long, aes(time, value, color = variable)) +
  guides(fill = "none")+
  geom_ma(n=5, size=1.2, linetype='solid')+
  scale_color_manual(name='Repetition',values=c('black','red','darkgreen','blue'))+
  labs(x = "Time (ms)",y = '')+
  geom_vline(xintercept = 0,linetype = "dashed" )+
  geom_hline(yintercept = 0,linetype = "dashed") +
  theme2 +
  coord_cartesian(ylim=c(-6,15)) + ggtitle('P4') +
  theme(legend.position = c(0.7, 0.9)) 



cp1 = plot_grid(p1,p2,p3,p4,p5,p6,p7,p8,p9,ncol=3,nrow=3)
save_plot('C:/Users/jscof/OneDrive - University of Missouri/eeg01_analyses_final/erp9fig.png',
          plot = cp1, ncol=3,nrow=3,base_height = 5, base_aspect_ratio = 1.42)
