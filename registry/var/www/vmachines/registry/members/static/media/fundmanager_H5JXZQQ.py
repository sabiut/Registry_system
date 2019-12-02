#sum function start
#all assets fund manager accounts
def sum_asset_fundmanager(request):
	#10102001CORP Account
	engine=create_engine('mssql+pymssql://sa:system1@10.0.150.20 /RBVData')
	connection=engine.connect()
	metadata=MetaData()
	fund=Table('gltrxdet',metadata,autoload=True,autoload_with=engine)
	stmt=select([func.sum(fund.columns.nat_balance),func.sum(fund.columns.balance)])

	stmt = stmt.where(fund.columns.account_code=='10102001CORP')
	results=connection.execute(stmt).fetchall()

	#calculating date MID Rate
	engine=create_engine('mssql+pymssql://sa:system1@10.0.150.20 /RBVCtrl')
	connection=engine.connect()
	metadata=MetaData()
	rate=Table('mccurtdt',metadata,autoload=True,autoload_with=engine)
	statmt=select([rate])
	statmt=statmt.where(and_(rate.columns.from_currency=='AUD', rate.columns.rate_type=='MID', rate.columns.convert_date=='736641'))
	da=connection.execute(statmt).fetchall()

	#10102002CORP Account
	engine=create_engine('mssql+pymssql://sa:system1@10.0.150.20 /RBVData')
	connection=engine.connect()
	metadata=MetaData()
	fund=Table('gltrxdet',metadata,autoload=True,autoload_with=engine)
	stmt=select([func.sum(fund.columns.nat_balance),func.sum(fund.columns.balance)])

	stmt = stmt.where(fund.columns.account_code=='10102002CORP')
	CORP10102002=connection.execute(stmt).fetchall()

	#calculating date MID Rate
	engine=create_engine('mssql+pymssql://sa:system1@10.0.150.20 /RBVCtrl')
	connection=engine.connect()
	metadata=MetaData()
	rate=Table('mccurtdt',metadata,autoload=True,autoload_with=engine)
	statmt=select([rate])
	statmt=statmt.where(and_(rate.columns.from_currency=='AUD', rate.columns.rate_type=='MID', rate.columns.convert_date=='736641'))
	CORP101020021=connection.execute(statmt).fetchall()

	#10102004CORP Account
	engine=create_engine('mssql+pymssql://sa:system1@10.0.150.20 /RBVData')
	connection=engine.connect()
	metadata=MetaData()
	fund=Table('gltrxdet',metadata,autoload=True,autoload_with=engine)
	stmt=select([func.sum(fund.columns.nat_balance),func.sum(fund.columns.balance)])

	stmt = stmt.where(fund.columns.account_code=='10102004CORP')
	CORP10102004=connection.execute(stmt).fetchall()

	#calculating date MID Rate
	engine=create_engine('mssql+pymssql://sa:system1@10.0.150.20 /RBVCtrl')
	connection=engine.connect()
	metadata=MetaData()
	rate=Table('mccurtdt',metadata,autoload=True,autoload_with=engine)
	statmt=select([rate])
	statmt=statmt.where(and_(rate.columns.from_currency=='AUD', rate.columns.rate_type=='MID', rate.columns.convert_date=='736641'))
	CORP101020041=connection.execute(statmt).fetchall()


	return render_to_response('allfundmanager.html',locals())

