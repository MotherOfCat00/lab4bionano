import statsmodels.api as st
import seaborn as sb
import matplotlib.pyplot as plt

c2 = [0, 0.00476, 0.00909, 0.01304, 0.01666, 0.02]

abs2 = [0.184, 0.298, 0.345, 0.396, 0.418, 0.438]
abs9 = [0.184, 0.675, 1.012, 1.11, 1.242, 1.389]

xc2 = st.add_constant(c2)
model = st.OLS(abs2, xc2)
results = model.fit()
with open(r'D:\bionano.txt', 'w') as fh:
    fh.write(results.summary().as_text())

print("podsumowanie", results.summary())
print("Parameters: ", results.params)
print("R2: ", results.rsquared)

xc2 = st.add_constant(c2)
model = st.OLS(abs9, xc2)
results = model.fit()
with open(r'D:\bionano9.txt', 'w') as fh:
    fh.write(results.summary().as_text())

print("podsumowanie", results.summary())
print("Parameters: ", results.params)
print("R2: ", results.rsquared)

plt.figure()
sb.regplot(x=c2, y=abs2)
plt.xlabel("C_m [mg/ml]")
plt.ylabel("Absorbance")

plt.figure()
sb.regplot(x=c2, y=abs9)
plt.xlabel("C_m [mg/ml]")
plt.ylabel("Absorbance")
plt.show()
