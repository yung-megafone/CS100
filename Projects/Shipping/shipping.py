# Property of NoviX Development
# https://nsic.dev/

# Variables
weight = 41.5

# Ground Shipping
gs_price = 0.0
gs_fee = 20.00
if weight <= 2.0:
  gs_price = (1.50 * weight) + gs_fee
elif weight >= 2.0 and weight <= 6.0:
  gs_price = (3.00 * weight) + gs_fee
elif weight >= 6.0 and weight <= 10.0:
  gs_price = (4.00 * weight) + gs_fee
elif weight >= 10.0:
  gs_price = (4.75 * weight) + gs_fee
print("Total cost for Standard is: " + str(gs_price) + " dollars for " + str(weight) + " pound packages")

# Ground Premium
gp_price = 125.00
print("Total cost for Premium is: " + str(gp_price) + " dollars for " + str(weight) + " pound packages")

# Drone Shipping
ds_price = 0.0
if weight <= 2.0:
  ds_price = (4.50 * weight)
elif weight >= 2.0 and weight <= 6.0:
  ds_price = (9.00 * weight)
elif weight >= 6.0 and weight <= 10.0:
  ds_price = (12.00 * weight)
elif weight > 10.0:
  ds_price = (14.25 * weight)
print("Total cost for Drone is: " + str(ds_price) + " dollars for " + str(weight) + " pound packages")

# If ground is cheaper then premium and drone
if gs_price <= gp_price and gs_price <= ds_price:
  print("Ground Standard is cheaper")

# If premium is cheaper than ground and drone
elif gp_price <= gs_price and ds_price:
  print("Premium Shipping is cheaper")

# If drone is cheaper than ground and premium
elif ds_price <= gs_price and gp_price:
  print("Drone Shipping is cheaper")

# This shouldn't be triggered, but better to have and not need it
else:
  print("Oops, we've encountered an error. Please try again")
