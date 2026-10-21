################################
### Mareike Burba, FE14 2025 ###
################################

import numpy as np
import xarray
import matplotlib.pyplot as plt

def plotme(ifile='./ecrad_meridian_direct_true_out.nc'):
  ds = xarray.open_dataset(ifile)
  
  fig,ax = plt.subplots(3,1,sharex=True)
  ax = ax.flatten()
  ds['cloud_cover_sw'].plot(ax=ax[0])
  
  ds['flux_dn_direct_sw_true'].plot(ax=ax[1], label='true')
  ds['flux_dn_sw'].isel(half_level=-1).plot(ax=ax[1], label='dn')
  ds['flux_dn_direct_sw'].isel(half_level=-1).plot(ls=':', ax=ax[1], label='delta E')
  ax[1].legend(title='SW direct dn sfc' )
  ax[1].set_ylim([0,1000])
  
  ds['flux_dn_direct_sw_true_clear'].plot(ax=ax[2], label='true')
  ds['flux_dn_direct_sw_clear'].isel(half_level=-1).plot(ls=':', ax=ax[2], label='delta E')
  ax[2].legend(title='SW clear direct dn sfc' )
  ax[2].set_ylim([0,1000])
  plt.show()
