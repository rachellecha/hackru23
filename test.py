import pickle

model = pickle.load(open('model_final.pkl','rb'))
print(model.predict(['04', '05', '15', '30', 'Edison', 'Metropark', 'Northeast Corrdr', 0.15]))