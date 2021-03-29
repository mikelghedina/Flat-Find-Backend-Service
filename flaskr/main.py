import NewService as s
import Flask 

coefsDict = s.get_coefs_by_district("Eixample")

#Dictionario de coeficientes, N de m2, N de Baños, N de habs
estimated_price = s.model_inference(coefsDict,80,1,3)
print(estimated_price)


