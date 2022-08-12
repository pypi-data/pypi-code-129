import pickle
import matplotlib.pyplot as plt
plt.style.use('seaborn')
from matplotlib.gridspec import GridSpec
from utility_functions import read_data, calculate_tractive_power, calculate_vsp, vsp_to_op_mod, op_mod_to_emission_rate, joule_to_kwh, convert_to_overall_mpg, energy_kj_to_ml, vsp_coeff, progress_bar
from Car import Car
# gasoline vehicle class
class GV(Car):

    def __init__(self,
                 excel_file_name = 'Data.xlsx',
                 sheet_name = 'Driving cycle',
                 mass = 1500,
                 frontal_area =2.27,
                 mu_rr =0.0127,
                 air_density =1.18,
                 c_d =0.28,
                 well_to_tank_CO2_emission_factor = 16.79                 
                 ):
        
        """
        excel_file_name (string)  : name of the excel file which contains the driving cycle data
        sheet_name      (string)  : name of the 'sheet' inside the excel file, which contains the driving cycle data.
                                    The provided excel file format is recommended to use. The 'sheet' should have the below 4 columns-
                                    time: in second
                                    speed: in meter per second
                                    time_unit : use the drop down list to choose the appropriate unit
                                    speed_unit : use the dropdown list to choose the appropriate unit                           
                                                
    
        mass                            (numeric) : vehicle mass with cargo in kg
        frontal_area                    (numeric) : vehicle frontal area in square meter
        mu_rr                           (numeric) : rolling resistance coefficient between tire and road surface
        air_density                     (numeric) : ambient air density in kg/m3
        c_d                             (numeric) : aerodynamic drag coefficient
        well_to_tank_CO2_emission_factor (numeric): typical value is 16.79 gm/MJ
            
        """
        
        super().__init__(excel_file_name, sheet_name, mass, frontal_area, mu_rr, air_density, c_d)
        self.well_to_tank_CO2_emission_factor = well_to_tank_CO2_emission_factor
        
        # add vsp, emission, and energy_kj columns to the main df
        print('\nPart [3/3]')
        for row in self.df.itertuples():
            idx = row.Index
            v = row.speed
            a = row.acc

            vsp = calculate_vsp (v, a, self.M, self.A, self.B, self.C, self.f)
            
            # calculate op_mod
            speed_t = v
            acc_t = a
            try:
                acc_t_1 = self.df.acc[idx - 1]
            except:
                acc_t_1 = 0
            try:
                acc_t_2 = self.df.acc[idx - 2]
            except:
                acc_t_2 = 0
            op_mod = vsp_to_op_mod (vsp, speed_t, acc_t, acc_t_1, acc_t_2)
            
            CO2                     = op_mod_to_emission_rate (self.df_emission_rate, op_mod, 'CO2')
            CO                      = op_mod_to_emission_rate (self.df_emission_rate, op_mod, 'CO')
            NOx                     = op_mod_to_emission_rate (self.df_emission_rate, op_mod, 'NOx')
            HC                      = op_mod_to_emission_rate (self.df_emission_rate, op_mod, 'HC')
            PM2_5_elemental_carbon  = op_mod_to_emission_rate (self.df_emission_rate, op_mod, 'PM2.5_elemental_carbon')
            PM2_5_organic_carbon    = op_mod_to_emission_rate (self.df_emission_rate, op_mod, 'PM2.5_organic_carbon')
           
            
            self.df.loc[idx, "vsp"]                      = vsp
            self.df.loc[idx, "op_mod"]                   = op_mod
            self.df.loc[idx, "CO2"]                      = CO2
            self.df.loc[idx, "CO"]                       = CO
            self.df.loc[idx, "NOx"]                      = NOx
            self.df.loc[idx, "HC"]                       = HC
            self.df.loc[idx, "PM2.5_elemental_carbon"]   = PM2_5_elemental_carbon
            self.df.loc[idx, "PM2.5_organic_carbon"]     = PM2_5_organic_carbon

            
            ##put a progress bar
            total_iteration = self.t
            progress_bar(total_iteration, idx + 1)
        
    
        
        
    def pump_to_wheel_CO2(self):
        CO2_sum = self.df.CO2.sum()
        return round(CO2_sum, 3)
    
    def pump_to_wheel_CO(self):
        CO_sum = self.df.CO.sum()
        return round(CO_sum, 3)
    
    def pump_to_wheel_NOx(self):
        NOx_sum = self.df.NOx.sum()
        return round(NOx_sum, 3)
    
    def pump_to_wheel_HC(self):
        HC_sum = self.df.HC.sum()
        return round(HC_sum, 3)
 
    def pump_to_wheel_CO2_per_km(self):
        value = self.pump_to_wheel_CO2()/self.d
        return round(value, 3)    
 
    def pump_to_wheel_CO_per_km(self):
        value = self.pump_to_wheel_CO()/self.d
        return round(value, 3)    
 
    def pump_to_wheel_NOx_per_km(self):
        value = self.pump_to_wheel_NOx()/self.d
        return round(value, 3)   
 
    def pump_to_wheel_HC_per_km(self):
        value = self.pump_to_wheel_HC()/self.d
        return round(value, 3)   
 
    
    def fuel_burnt(self):
        HC = self.pump_to_wheel_NOx()
        CO = self.pump_to_wheel_CO()
        CO2 = self.pump_to_wheel_CO2()
        density = 750
        W_c = 0.866
        fuel_sum = (0.866*HC + 0.429*CO + 0.273*CO2)*1000/(density*W_c)
        return round(fuel_sum, 3)
    
    def mpg(self):
        fuel = self.fuel_burnt()
        value = (self.d/1.60934)/(fuel/3785.412)
        return round(value, 3)


    def well_to_pump_CO2(self):
        gasoline = self.fuel_burnt()
        value = gasoline*34.2*self.well_to_tank_CO2_emission_factor/1000
        return round(value, 3)
        
    def well_to_wheel_CO2(self):
        value = self.pump_to_wheel_CO2() + self.well_to_pump_CO2()
        return round(value, 3)
    
    def well_to_wheel_CO2_per_km(self):
        value = self.well_to_wheel_CO2()/self.d
        return round(value, 3)


     
#------------------------------------------------------------------------------
if __name__ == '__main__':    
    
    g = GV("Data.xlsx", "Driving cycle", mass=2850)
    
    g.plot_driving_cycle()
    g.plot_tractive_power()
    g.plot_speed_histogram()
    
    print('\n\nGeneral statistics of the driving cycle\n-------------------------------------------------')
    print(f'Distance traveled                       : {g.distance()} km')
    print(f'Average speed                           : {g.average_speed()} KMPH')
    print(f'Standaed deviation of speed             : {g.speed_std()} KMPH')
    print(f'Number of stops per kilometer           : {g.no_of_stops_per_km()}')
    print(f'Average acceleration                    : {g.acc_avg()} m/s2')
    print(f'Average deceleration                    : {g.dec_avg()} m/s2')
    print(f'Percentage of time on acceleration mode : {g.acc_mode()}%')
    print(f'Percentage of time on deceleration mode : {g.dec_mode()}%')
    print(f'Percetage of time on idling mode        : {g.idling_mode()}%')
    
    print('\n\nStatistics for Gasoline vehicle\n-------------------------------------------------')
    print(f'Tailpipe CO2 emission                   : {g.pump_to_wheel_CO2()} grams')
    print(f'Tailpipe CO emission                    : {g.pump_to_wheel_CO()} grams')
    print(f'Tailpipe NOx emission                   : {g.pump_to_wheel_NOx()} grams')
    print(f'Tailpipe HC emission                    : {g.pump_to_wheel_HC()} grams')
    
    print(f'Tailpipe CO2 emission per km            : {g.pump_to_wheel_CO2_per_km()} grams/km')
    print(f'Tailpipe CO  emission per km            : {g.pump_to_wheel_CO_per_km()} grams/km')
    print(f'Tailpipe NOx emission per km            : {g.pump_to_wheel_NOx_per_km()} grams/km')
    print(f'Tailpipe HC  emission per km            : {g.pump_to_wheel_HC_per_km()} grams/km')

    print(f'Well to Pump CO2 emission               : {g.well_to_pump_CO2()} grams')
    print(f'Well to Wheel CO2 emission              : {g.well_to_wheel_CO2()} grams')
    print(f'Well to Wheel CO2 emission per km       : {g.well_to_wheel_CO2_per_km()} grams/km')
    
    print(f'Fuel burnt                              : {g.fuel_burnt()} ml')
    print(f'Miles per Gallon (MPG)                  : {g.mpg()}')
    
