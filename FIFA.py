import pandas as pd
data_frame = pd.read_csv('data.csv')
data_frame


Unnamed: 0	ID	Name	Age	Photo	Nationality	Flag	Overall	Potential	Club	...	Composure	Marking	StandingTackle	SlidingTackle	GKDiving	GKHandling	GKKicking	GKPositioning	GKReflexes	Release Clause
0	0	158023	L. Messi	31	https://cdn.sofifa.org/players/4/19/158023.png	Argentina	https://cdn.sofifa.org/flags/52.png	94	94	FC Barcelona	...	96.0	33.0	28.0	26.0	6.0	11.0	15.0	14.0	8.0	€226.5M
1	1	20801	Cristiano Ronaldo	33	https://cdn.sofifa.org/players/4/19/20801.png	Portugal	https://cdn.sofifa.org/flags/38.png	94	94	Juventus	...	95.0	28.0	31.0	23.0	7.0	11.0	15.0	14.0	11.0	€127.1M
2	2	190871	Neymar Jr	26	https://cdn.sofifa.org/players/4/19/190871.png	Brazil	https://cdn.sofifa.org/flags/54.png	92	93	Paris Saint-Germain	...	94.0	27.0	24.0	33.0	9.0	9.0	15.0	15.0	11.0	€228.1M
3	3	193080	De Gea	27	https://cdn.sofifa.org/players/4/19/193080.png	Spain	https://cdn.sofifa.org/flags/45.png	91	93	Manchester United	...	68.0	15.0	21.0	13.0	90.0	85.0	87.0	88.0	94.0	€138.6M
4	4	192985	K. De Bruyne	27	https://cdn.sofifa.org/players/4/19/192985.png	Belgium	https://cdn.sofifa.org/flags/7.png	91	92	Manchester City	...	88.0	68.0	58.0	51.0	15.0	13.0	5.0	10.0	13.0	€196.4M
5	5	183277	E. Hazard	27	https://cdn.sofifa.org/players/4/19/183277.png	Belgium	https://cdn.sofifa.org/flags/7.png	91	91	Chelsea	...	91.0	34.0	27.0	22.0	11.0	12.0	6.0	8.0	8.0	€172.1M
6	6	177003	L. Modrić	32	https://cdn.sofifa.org/players/4/19/177003.png	Croatia	https://cdn.sofifa.org/flags/10.png	91	91	Real Madrid	...	84.0	60.0	76.0	73.0	13.0	9.0	7.0	14.0	9.0	€137.4M
7	7	176580	L. Suárez	31	https://cdn.sofifa.org/players/4/19/176580.png	Uruguay	https://cdn.sofifa.org/flags/60.png	91	91	FC Barcelona	...	85.0	62.0	45.0	38.0	27.0	25.0	31.0	33.0	37.0	€164M
8	8	155862	Sergio Ramos	32	https://cdn.sofifa.org/players/4/19/155862.png	Spain	https://cdn.sofifa.org/flags/45.png	91	91	Real Madrid	...	82.0	87.0	92.0	91.0	11.0	8.0	9.0	7.0	11.0	€104.6M
9	9	200389	J. Oblak	25	https://cdn.sofifa.org/players/4/19/200389.png	Slovenia	https://cdn.sofifa.org/flags/44.png	90	93	Atlético Madrid	...	70.0	27.0	12.0	18.0	86.0	92.0	78.0	88.0	89.0	€144.5M
10	10	188545	R. Lewandowski	29	https://cdn.sofifa.org/players/4/19/188545.png	Poland	https://cdn.sofifa.org/flags/37.png	90	90	FC Bayern München	...	86.0	34.0	42.0	19.0	15.0	6.0	12.0	8.0	10.0	€127.1M
11	11	182521	T. Kroos	28	https://cdn.sofifa.org/players/4/19/182521.png	Germany	https://cdn.sofifa.org/flags/21.png	90	90	Real Madrid	...	85.0	72.0	79.0	69.0	10.0	11.0	13.0	7.0	10.0	€156.8M
12	12	182493	D. Godín	32	https://cdn.sofifa.org/players/4/19/182493.png	Uruguay	https://cdn.sofifa.org/flags/60.png	90	90	Atlético Madrid	...	82.0	90.0	89.0	89.0	6.0	8.0	15.0	5.0	15.0	€90.2M
13	13	168542	David Silva	32	https://cdn.sofifa.org/players/4/19/168542.png	Spain	https://cdn.sofifa.org/flags/45.png	90	90	Manchester City	...	93.0	59.0	53.0	29.0	6.0	15.0	7.0	6.0	12.0	€111M
14	14	215914	N. Kanté	27	https://cdn.sofifa.org/players/4/19/215914.png	France	https://cdn.sofifa.org/flags/18.png	89	90	Chelsea	...	85.0	90.0	91.0	85.0	15.0	12.0	10.0	7.0	10.0	€121.3M
15	15	211110	P. Dybala	24	https://cdn.sofifa.org/players/4/19/211110.png	Argentina	https://cdn.sofifa.org/flags/52.png	89	94	Juventus	...	84.0	23.0	20.0	20.0	5.0	4.0	4.0	5.0	8.0	€153.5M
16	16	202126	H. Kane	24	https://cdn.sofifa.org/players/4/19/202126.png	England	https://cdn.sofifa.org/flags/14.png	89	91	Tottenham Hotspur	...	89.0	56.0	36.0	38.0	8.0	10.0	11.0	14.0	11.0	€160.7M
17	17	194765	A. Griezmann	27	https://cdn.sofifa.org/players/4/19/194765.png	France	https://cdn.sofifa.org/flags/18.png	89	90	Atlético Madrid	...	87.0	59.0	47.0	48.0	14.0	8.0	14.0	13.0	14.0	€165.8M
18	18	192448	M. ter Stegen	26	https://cdn.sofifa.org/players/4/19/192448.png	Germany	https://cdn.sofifa.org/flags/21.png	89	92	FC Barcelona	...	69.0	25.0	13.0	10.0	87.0	85.0	88.0	85.0	90.0	€123.3M
19	19	192119	T. Courtois	26	https://cdn.sofifa.org/players/4/19/192119.png	Belgium	https://cdn.sofifa.org/flags/7.png	89	90	Real Madrid	...	66.0	20.0	18.0	16.0	85.0	91.0	72.0	86.0	88.0	€113.7M
20	20	189511	Sergio Busquets	29	https://cdn.sofifa.org/players/4/19/189511.png	Spain	https://cdn.sofifa.org/flags/45.png	89	89	FC Barcelona	...	90.0	90.0	86.0	80.0	5.0	8.0	13.0	9.0	13.0	€105.6M
21	21	179813	E. Cavani	31	https://cdn.sofifa.org/players/4/19/179813.png	Uruguay	https://cdn.sofifa.org/flags/60.png	89	89	Paris Saint-Germain	...	82.0	52.0	45.0	39.0	12.0	5.0	13.0	13.0	10.0	€111M
22	22	167495	M. Neuer	32	https://cdn.sofifa.org/players/4/19/167495.png	Germany	https://cdn.sofifa.org/flags/21.png	89	89	FC Bayern München	...	70.0	17.0	10.0	11.0	90.0	86.0	91.0	87.0	87.0	€62.7M
23	23	153079	S. Agüero	30	https://cdn.sofifa.org/players/4/19/153079.png	Argentina	https://cdn.sofifa.org/flags/52.png	89	89	Manchester City	...	90.0	30.0	20.0	12.0	13.0	15.0	6.0	11.0	14.0	€119.3M
24	24	138956	G. Chiellini	33	https://cdn.sofifa.org/players/4/19/138956.png	Italy	https://cdn.sofifa.org/flags/27.png	89	89	Juventus	...	84.0	93.0	93.0	90.0	3.0	3.0	2.0	4.0	3.0	€44.6M
25	25	231747	K. Mbappé	19	https://cdn.sofifa.org/players/4/19/231747.png	France	https://cdn.sofifa.org/flags/18.png	88	95	Paris Saint-Germain	...	86.0	34.0	34.0	32.0	13.0	5.0	7.0	11.0	6.0	€166.1M
26	26	209331	M. Salah	26	https://cdn.sofifa.org/players/4/19/209331.png	Egypt	https://cdn.sofifa.org/flags/111.png	88	89	Liverpool	...	91.0	38.0	43.0	41.0	14.0	14.0	9.0	11.0	14.0	€137.3M
27	27	200145	Casemiro	26	https://cdn.sofifa.org/players/4/19/200145.png	Brazil	https://cdn.sofifa.org/flags/54.png	88	90	Real Madrid	...	84.0	88.0	90.0	87.0	13.0	14.0	16.0	12.0	12.0	€126.4M
28	28	198710	J. Rodríguez	26	https://cdn.sofifa.org/players/4/19/198710.png	Colombia	https://cdn.sofifa.org/flags/56.png	88	89	FC Bayern München	...	87.0	52.0	41.0	44.0	15.0	15.0	15.0	5.0	14.0	NaN
29	29	198219	L. Insigne	27	https://cdn.sofifa.org/players/4/19/198219.png	Italy	https://cdn.sofifa.org/flags/27.png	88	88	Napoli	...	83.0	51.0	24.0	22.0	8.0	4.0	14.0	9.0	10.0	€105.4M
...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...	...
18177	18177	238550	R. Roache	18	https://cdn.sofifa.org/players/4/19/238550.png	Republic of Ireland	https://cdn.sofifa.org/flags/25.png	48	69	Blackpool	...	49.0	18.0	16.0	11.0	6.0	9.0	11.0	7.0	12.0	€193K
18178	18178	243158	L. Wahlstedt	18	https://cdn.sofifa.org/players/4/19/243158.png	Sweden	https://cdn.sofifa.org/flags/46.png	48	65	Dalkurd FF	...	28.0	16.0	11.0	10.0	47.0	46.0	50.0	45.0	51.0	€94K
18179	18179	246243	J. Williams	17	https://cdn.sofifa.org/players/4/19/246243.png	England	https://cdn.sofifa.org/flags/14.png	48	64	Northampton Town	...	37.0	42.0	51.0	49.0	14.0	11.0	7.0	11.0	8.0	€119K
18180	18180	221669	M. Hurst	22	https://cdn.sofifa.org/players/4/19/221669.png	Scotland	https://cdn.sofifa.org/flags/42.png	48	58	St. Johnstone FC	...	28.0	12.0	15.0	16.0	45.0	49.0	50.0	50.0	45.0	€78K
18181	18181	245734	C. Maher	17	https://cdn.sofifa.org/players/4/19/245734.png	Republic of Ireland	https://cdn.sofifa.org/flags/25.png	48	66	Bray Wanderers	...	38.0	43.0	49.0	45.0	8.0	10.0	12.0	9.0	10.0	€109K
18182	18182	246001	Y. Góez	18	https://cdn.sofifa.org/players/4/19/246001.png	Colombia	https://cdn.sofifa.org/flags/56.png	48	65	Atlético Nacional	...	38.0	44.0	42.0	46.0	9.0	15.0	15.0	8.0	6.0	€101K
18183	18183	53748	K. Pilkington	44	https://cdn.sofifa.org/players/4/19/53748.png	England	https://cdn.sofifa.org/flags/14.png	48	48	Cambridge United	...	56.0	15.0	15.0	13.0	45.0	48.0	44.0	49.0	46.0	NaN
18184	18184	241657	D. Horton	18	https://cdn.sofifa.org/players/4/19/241657.png	England	https://cdn.sofifa.org/flags/14.png	48	55	Lincoln City	...	42.0	47.0	49.0	53.0	12.0	5.0	12.0	14.0	15.0	€78K
18185	18185	243961	E. Tweed	19	https://cdn.sofifa.org/players/4/19/243961.png	Republic of Ireland	https://cdn.sofifa.org/flags/25.png	48	59	Derry City	...	43.0	39.0	39.0	48.0	6.0	11.0	9.0	5.0	8.0	€88K
18186	18186	240917	Zhang Yufeng	20	https://cdn.sofifa.org/players/4/19/240917.png	China PR	https://cdn.sofifa.org/flags/155.png	47	64	Beijing Renhe FC	...	39.0	53.0	41.0	51.0	15.0	7.0	14.0	6.0	8.0	€167K
18187	18187	240158	C. Ehlich	19	https://cdn.sofifa.org/players/4/19/240158.png	Germany	https://cdn.sofifa.org/flags/21.png	47	59	SpVgg Unterhaching	...	47.0	40.0	42.0	42.0	13.0	12.0	11.0	15.0	12.0	€66K
18188	18188	240927	L. Collins	17	https://cdn.sofifa.org/players/4/19/240927.png	Wales	https://cdn.sofifa.org/flags/50.png	47	62	Newport County	...	46.0	33.0	38.0	41.0	5.0	12.0	8.0	13.0	10.0	€143K
18189	18189	240160	A. Kaltner	18	https://cdn.sofifa.org/players/4/19/240160.png	Germany	https://cdn.sofifa.org/flags/21.png	47	61	SpVgg Unterhaching	...	37.0	28.0	15.0	22.0	15.0	5.0	14.0	12.0	8.0	€125K
18190	18190	245569	L. Watkins	18	https://cdn.sofifa.org/players/4/19/245569.png	England	https://cdn.sofifa.org/flags/14.png	47	67	Cambridge United	...	46.0	35.0	44.0	47.0	13.0	7.0	14.0	10.0	8.0	€165K
18191	18191	245570	J. Norville-Williams	18	https://cdn.sofifa.org/players/4/19/245570.png	England	https://cdn.sofifa.org/flags/14.png	47	65	Cambridge United	...	36.0	45.0	42.0	46.0	15.0	13.0	6.0	14.0	12.0	€119K
18192	18192	245571	S. Squire	18	https://cdn.sofifa.org/players/4/19/245571.png	England	https://cdn.sofifa.org/flags/14.png	47	64	Cambridge United	...	38.0	41.0	41.0	44.0	11.0	11.0	8.0	12.0	13.0	€119K
18193	18193	244823	N. Fuentes	18	https://cdn.sofifa.org/players/4/19/244823.png	Chile	https://cdn.sofifa.org/flags/55.png	47	64	Unión Española	...	32.0	41.0	48.0	48.0	6.0	10.0	6.0	12.0	11.0	€99K
18194	18194	245862	J. Milli	18	https://cdn.sofifa.org/players/4/19/245862.png	Italy	https://cdn.sofifa.org/flags/27.png	47	65	Lecce	...	23.0	6.0	10.0	11.0	52.0	52.0	52.0	40.0	44.0	€109K
18195	18195	243582	S. Griffin	18	https://cdn.sofifa.org/players/4/19/243582.png	Republic of Ireland	https://cdn.sofifa.org/flags/25.png	47	67	Waterford FC	...	41.0	44.0	37.0	48.0	13.0	14.0	12.0	7.0	13.0	€153K
18196	18196	238477	K. Fujikawa	19	https://cdn.sofifa.org/players/4/19/238477.png	Japan	https://cdn.sofifa.org/flags/163.png	47	61	Júbilo Iwata	...	35.0	41.0	44.0	54.0	10.0	12.0	6.0	11.0	8.0	€113K
18197	18197	246167	D. Holland	18	https://cdn.sofifa.org/players/4/19/246167.png	Republic of Ireland	https://cdn.sofifa.org/flags/25.png	47	61	Cork City	...	52.0	41.0	47.0	38.0	13.0	6.0	9.0	10.0	15.0	€88K
18198	18198	242844	J. Livesey	18	https://cdn.sofifa.org/players/4/19/242844.png	England	https://cdn.sofifa.org/flags/14.png	47	70	Burton Albion	...	34.0	15.0	11.0	13.0	46.0	52.0	58.0	42.0	48.0	€165K
18199	18199	244677	M. Baldisimo	18	https://cdn.sofifa.org/players/4/19/244677.png	Canada	https://cdn.sofifa.org/flags/70.png	47	69	Vancouver Whitecaps FC	...	40.0	48.0	49.0	49.0	7.0	7.0	9.0	14.0	15.0	€175K
18200	18200	231381	J. Young	18	https://cdn.sofifa.org/players/4/19/231381.png	Scotland	https://cdn.sofifa.org/flags/42.png	47	62	Swindon Town	...	50.0	15.0	17.0	14.0	11.0	15.0	12.0	12.0	11.0	€143K
18201	18201	243413	D. Walsh	18	https://cdn.sofifa.org/players/4/19/243413.png	Republic of Ireland	https://cdn.sofifa.org/flags/25.png	47	68	Waterford FC	...	43.0	44.0	47.0	53.0	9.0	10.0	9.0	11.0	13.0	€153K
18202	18202	238813	J. Lundstram	19	https://cdn.sofifa.org/players/4/19/238813.png	England	https://cdn.sofifa.org/flags/14.png	47	65	Crewe Alexandra	...	45.0	40.0	48.0	47.0	10.0	13.0	7.0	8.0	9.0	€143K
18203	18203	243165	N. Christoffersson	19	https://cdn.sofifa.org/players/4/19/243165.png	Sweden	https://cdn.sofifa.org/flags/46.png	47	63	Trelleborgs FF	...	42.0	22.0	15.0	19.0	10.0	9.0	9.0	5.0	12.0	€113K
18204	18204	241638	B. Worman	16	https://cdn.sofifa.org/players/4/19/241638.png	England	https://cdn.sofifa.org/flags/14.png	47	67	Cambridge United	...	41.0	32.0	13.0	11.0	6.0	5.0	10.0	6.0	13.0	€165K
18205	18205	246268	D. Walker-Rice	17	https://cdn.sofifa.org/players/4/19/246268.png	England	https://cdn.sofifa.org/flags/14.png	47	66	Tranmere Rovers	...	46.0	20.0	25.0	27.0	14.0	6.0	14.0	8.0	9.0	€143K
18206	18206	246269	G. Nugent	16	https://cdn.sofifa.org/players/4/19/246269.png	England	https://cdn.sofifa.org/flags/14.png	46	66	Tranmere Rovers	...	43.0	40.0	43.0	50.0	10.0	15.0	9.0	12.0	9.0	€165K
18207 rows × 89 columns

data_frame.describe()


Unnamed: 0	ID	Age	Overall	Potential	Special	International Reputation	Weak Foot	Skill Moves	Jersey Number	...	Penalties	Composure	Marking	StandingTackle	SlidingTackle	GKDiving	GKHandling	GKKicking	GKPositioning	GKReflexes
count	18207.000000	18207.000000	18207.000000	18207.000000	18207.000000	18207.000000	18159.000000	18159.000000	18159.000000	18147.000000	...	18159.000000	18159.000000	18159.000000	18159.000000	18159.000000	18159.000000	18159.000000	18159.000000	18159.000000	18159.000000
mean	9103.000000	214298.338606	25.122206	66.238699	71.307299	1597.809908	1.113222	2.947299	2.361308	19.546096	...	48.548598	58.648274	47.281623	47.697836	45.661435	16.616223	16.391596	16.232061	16.388898	16.710887
std	5256.052511	29965.244204	4.669943	6.908930	6.136496	272.586016	0.394031	0.660456	0.756164	15.947765	...	15.704053	11.436133	19.904397	21.664004	21.289135	17.695349	16.906900	16.502864	17.034669	17.955119
min	0.000000	16.000000	16.000000	46.000000	48.000000	731.000000	1.000000	1.000000	1.000000	1.000000	...	5.000000	3.000000	3.000000	2.000000	3.000000	1.000000	1.000000	1.000000	1.000000	1.000000
25%	4551.500000	200315.500000	21.000000	62.000000	67.000000	1457.000000	1.000000	3.000000	2.000000	8.000000	...	39.000000	51.000000	30.000000	27.000000	24.000000	8.000000	8.000000	8.000000	8.000000	8.000000
50%	9103.000000	221759.000000	25.000000	66.000000	71.000000	1635.000000	1.000000	3.000000	2.000000	17.000000	...	49.000000	60.000000	53.000000	55.000000	52.000000	11.000000	11.000000	11.000000	11.000000	11.000000
75%	13654.500000	236529.500000	28.000000	71.000000	75.000000	1787.000000	1.000000	3.000000	3.000000	26.000000	...	60.000000	67.000000	64.000000	66.000000	64.000000	14.000000	14.000000	14.000000	14.000000	14.000000
max	18206.000000	246620.000000	45.000000	94.000000	95.000000	2346.000000	5.000000	5.000000	5.000000	99.000000	...	92.000000	96.000000	94.000000	93.000000	91.000000	90.000000	92.000000	91.000000	90.000000	94.000000
8 rows × 44 columns

data_frame.values


array([[0, 158023, 'L. Messi', ..., 14.0, 8.0, '€226.5M'],
       [1, 20801, 'Cristiano Ronaldo', ..., 14.0, 11.0, '€127.1M'],
       [2, 190871, 'Neymar Jr', ..., 15.0, 11.0, '€228.1M'],
       ...,
       [18204, 241638, 'B. Worman', ..., 6.0, 13.0, '€165K'],
       [18205, 246268, 'D. Walker-Rice', ..., 8.0, 9.0, '€143K'],
       [18206, 246269, 'G. Nugent', ..., 12.0, 9.0, '€165K']],
      dtype=object)
      
      
      
df1 = pd.DataFrame(data_frame, columns=['Name', 'Wage', 'Value'])
def value_to_float(x):
    if type(x) == float or type(x) == int:
        return x
    if 'K' in x:
        if len(x) > 1:
            return float(x.replace('K', '')) * 1000
        return 1000.0
    if 'M' in x:
        if len(x) > 1:
            return float(x.replace('M', '')) * 1000000
        return 1000000.0
    if 'B' in x:
        return float(x.replace('B', '')) * 1000000000
    return 0.0

wage = df1['Wage'].replace('[\€,]', '', regex=True).apply(value_to_float)
value = df1['Value'].replace('[\€,]', '', regex=True).apply(value_to_float)

df1['Wage'] = wage
df1['Value'] = value

df1['difference'] = df1['Value'] - df1['Wage']
df1.sort_values('difference', ascending=False)


Name	Wage	Value	difference
2	Neymar Jr	290000.0	118500000.0	118210000.0
0	L. Messi	565000.0	110500000.0	109935000.0
4	K. De Bruyne	355000.0	102000000.0	101645000.0
5	E. Hazard	340000.0	93000000.0	92660000.0
15	P. Dybala	205000.0	89000000.0	88795000.0
16	H. Kane	205000.0	83500000.0	83295000.0
25	K. Mbappé	100000.0	81000000.0	80900000.0
7	L. Suárez	455000.0	80000000.0	79545000.0
17	A. Griezmann	145000.0	78000000.0	77855000.0
10	R. Lewandowski	205000.0	77000000.0	76795000.0
1	Cristiano Ronaldo	405000.0	77000000.0	76595000.0
11	T. Kroos	355000.0	76500000.0	76145000.0
31	C. Eriksen	205000.0	73500000.0	73295000.0
30	Isco	315000.0	73500000.0	73185000.0
3	De Gea	260000.0	72000000.0	71740000.0
26	M. Salah	255000.0	69500000.0	69245000.0
28	J. Rodríguez	315000.0	69500000.0	69185000.0
32	Coutinho	340000.0	69500000.0	69160000.0
9	J. Oblak	94000.0	68000000.0	67906000.0
6	L. Modrić	420000.0	67000000.0	66580000.0
43	M. Icardi	130000.0	64500000.0	64370000.0
23	S. Agüero	300000.0	64500000.0	64200000.0
45	P. Pogba	210000.0	64000000.0	63790000.0
14	N. Kanté	225000.0	63000000.0	62775000.0
47	R. Lukaku	230000.0	62500000.0	62270000.0
29	L. Insigne	165000.0	62000000.0	61835000.0
55	L. Sané	195000.0	61000000.0	60805000.0
21	E. Cavani	200000.0	60000000.0	59800000.0
13	David Silva	285000.0	60000000.0	59715000.0
36	G. Bale	355000.0	60000000.0	59645000.0
...	...	...	...	...
5272	C. Deac	0.0	0.0	0.0
14054	P. Halder	0.0	0.0	0.0
4823	P. Anton	0.0	0.0	0.0
5245	R. Cardozo	0.0	0.0	0.0
2984	M. Borjan	0.0	0.0	0.0
6841	N. Bancu	0.0	0.0	0.0
7990	B. Mitrev	0.0	0.0	0.0
5126	L. Cáceda	0.0	0.0	0.0
9568	C. Gonzáles	0.0	0.0	0.0
8057	D. Mendiseca	0.0	0.0	0.0
8061	S. Gbohouo	0.0	0.0	0.0
11247	A. Cicâldău	0.0	0.0	0.0
2999	K. Rausch	0.0	0.0	0.0
17436	D. Lalhlimpuia	0.0	0.0	0.0
8273	D. Furman	0.0	0.0	0.0
16539	L. Lalruatthara	0.0	0.0	0.0
3037	Y. Banana	0.0	0.0	0.0
5082	J. Paredes	0.0	0.0	0.0
4945	H. Vaca	0.0	0.0	0.0
17672	R. Kawai	1000.0	0.0	-1000.0
10356	F. Kippe	1000.0	0.0	-1000.0
12453	W. Díaz	1000.0	0.0	-1000.0
14129	Y. Nakazawa	1000.0	0.0	-1000.0
18183	K. Pilkington	1000.0	0.0	-1000.0
17726	T. Warner	1000.0	0.0	-1000.0
17752	S. Phillips	1000.0	0.0	-1000.0
12192	H. Sulaimani	3000.0	0.0	-3000.0
3550	S. Nakamura	4000.0	0.0	-4000.0
4228	B. Nivet	5000.0	0.0	-5000.0
864	Hilton	18000.0	0.0	-18000.0
18207 rows × 4 columns


import seaborn as sns
sns.set()

graph = sns.scatterplot(x='Wage', y='Value', data=df1)
graph
<matplotlib.axes._subplots.AxesSubplot at 0x121b01198>

from bokeh.plotting import figure,show
from bokeh.models import HoverTool

TOOLTIPS = HoverTool(tooltips=[
    ("index", "$index"),
    ("(Wage,Value)", "(@Wage, @Value)"),
    ("Name", "@Name")]
)

p = figure(title="Soccer 2019", x_axis_label='Wage', y_axis_label='Value', plot_width=700, plot_height=700, tools=[TOOLTIPS])
p.circle('Wage', 'Value', size=10, source=df1)
show(p)
 
