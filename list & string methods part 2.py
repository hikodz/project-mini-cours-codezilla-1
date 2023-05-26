 
# salaries list
#!
salaries = [
64700, 23100, 81800, 31300, 35500, 84300, 25900,
15500, 24500, 69000, 40100, 86100, 17000, 55800,
17400, 15400, 93500, 30000, 68500, 70400, 60200,
65500, 57100, 20800, 19500, 96200, 43400, 15500,
36200, 16100, 21300, 63500, 83900, 85600, 40700,
75700, 53700, 18400, 18400, 48800, 72300, 64600,
77700, 97300, 64700, 53500, 34300, 76700, 41200,
78300, 76000, 23600, 31800, 46800, 67600, 96700,
60000, 33500, 96300, 65800, 80100, 59500, 78600,
42500, 37700, 58800, 92300, 76000, 65300, 89600,
22500, 98200, 99100, 38600, 42200, 16400, 17200,
97600, 60500, 20800, 78500, 71100, 43700, 46500,
51200, 87600, 68900, 85400, 44400, 53600, 91700,
93200, 13300, 14200, 49500, 56600, 44400, 89700,
21300, 100000, 63900, 78600, 61800, 50400, 39700,
23100, 26300, 70700, 82700, 11400, 55000, 82900,
54300,78300, 44900, 12600, 21500, 87500, 32200,
47400, 13800, 54000, 11600, 68100, 94700, 51000,
20800, 80100, 53700, 25000, 55900, 11700, 61300,
93800, 72800, 46200, 39800, 96900, 66700, 55400,
40600, 87000,93400, 74800, 84500, 17100, 38800,
49100, 64000, 69200, 10540, 12300, 16900, 14500,
105540, 21080, 12760, 19960, 13960, 14280, 12680,
17000, 15960,12760, 113240, 17400, 15500, 15080,
19240, 18360, 13480, 14120,17000, 11000, 11720,
117400, 18840, 21100, 9480, 10440, 17560,11400,
9640, 17000, 20360, 9720, 14040, 8792, 10200,
13880, 11960
]
#!
# extra salary list
extra_salaries = [
13300, 20500, 12100, 17200, 10600, 16600, 18100,
17600, 20400, 12600, 12300, 18800, 15300, 14300,
19800, 11500, 12500, 12700, 18300, 17800, 20500,
13800, 20300, 11100, 15300, 11200, 18300, 12500,
16800, 12100, 20200, 18700, 20100, 13700, 13400,
19600, 19200, 15800, 10900, 19500, 13000, 17400,
10600, 13900, 10800, 14800, 16600, 19200, 18300,
14700, 19100, 12100, 12400, 16300, 13900, 15700,
17700, 12100, 13000, 13700, 15300, 14800, 19400,
13700, 18000, 11300, 14400, 20200, 17600, 19900,
13300, 19100, 17400, 12400, 19200, 11100, 18700
]
# Section 8: Python Conditionals & Lists
#list & string methods part 2

#! line 1:
extend_lists = salaries.extend(extra_salaries)
max_sal = max(salaries)
salaries.sort()
top_sal = salaries[-5:]
print(f'Maximum salary: {max_sal:,} EGP\nTop 5 salaries: {top_sal} EGP\n')
print('-'*25)

#! line 2:
min_sal = min(salaries)
salaries.sort()
bot_sal = salaries[:5]
print(f'Bottom salary: {min_sal:,} EGP\nBottom 5 salaries: {bot_sal} EGP\n')
print('-'*25)

#! line 3:
aver_sal = sum(salaries) / len(salaries)
print(f'Average salary: {aver_sal:,.0f} EGP\n{"-" * 25}')

#! line 4:
serch_salery = salaries.count(15500)
print(f'Number of people with salary = 15,500 EGP: {serch_salery} people')

