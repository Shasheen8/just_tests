import numpy as np
import vectormath as vmath

# Single Vectors
v = vmath.Vector3(5, 0, 0)
v.normalize()
print(v)                          # >> [1, 0, 0]
print(v.x)                        # >> 1.0

# VectorArrays are much faster than a for loop over Vectors
v_array = vmath.Vector3Array([[4, 0, 0], [0, 2, 0], [0, 0, 3]])
print(v_array.x)                  # >> [4, 0, 0]
print(v_array.length)             # >> [4, 2, 3]
print(v_array.normalize())        # >> [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# Vectors can be accessed individually or in slices
print(type(v_array[1:]))          # >> vectormath.Vector3Array
print(type(v_array[2]))           # >> vectormath.Vector3

# All these classes are just numpy arrays
print(isinstance(v, np.ndarray))  # >> True
print(type(v_array[1:, 1:]))      # >> numpy.ndarray



Service dependencies
Dunlop. To run front-end we need to connect to a Dunlop instance
BFF. To run front-end we have to connect to the bff. This can be achieved with docker compose. If you are running a local Dunlop instance, this is not needed, as the BFF is part of the Dunlop dependencies
Schumacher: front-end should be connected to a schumacher instance. This is required for front-end to proxy requests for any schumacher page.
Flagr: front-end supports server-side flags by connecting directly to Flagr.
Create a .env file with the following content:

AWS_ACCESS_KEY_ID=(1Password entry name node-bff-app)
AWS_SECRET_ACCESS_KEY=(1Password entry name node-bff-app)
DUNLOP_ROOT=some_dunlop_root
DUNLOP_API_KEY=some_dunlop_api_key
ENABLE_INTROSPECTION=true
STORYBLOK_API_KEY=storyblok_api_token: (1Password entry name turo-storyblok-cdn)
STORYBLOK_INCLUDE_DRAFTS=true
VEHICLE_SEARCH_SERVICE_URL=http://localhost:8081
