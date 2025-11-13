# # nutrients=[
# #     [250,200,150,50,100],
# #     [30,4,10,4,8],
# #     [5,1,1,0,4]
# # ]
# # print(len(nutrients))
# # print(3**2*2)
# x=[1,2,3]
# y=[1,2,2]

# ct=sum(a*b for a,b in zip(x,y))
# print(ct)



nutrient_totals = [0] * len(nutrients)

for i in range(len(nutrients)):            # nutrient index (যেমন calories, protein, fat)
    total = 0                              # এই nutrient-এর total value
    for j in range(len(foods)):            # প্রতিটি খাবারের জন্য
        total += amounts[j] * nutrients[i][j]  # ওই nutrient-এর পরিমাণ যোগ করো
    nutrient_totals[i] = total             # মোট nutrient যোগফল সংরক্ষণ করো
