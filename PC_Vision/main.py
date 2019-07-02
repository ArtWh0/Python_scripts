def view_bytes(fpath, delim=''):
	ret=[]
	view=[]
	i=0
	new=''
	with open(fpath, 'br') as f:
		for chunk in iter(lambda: f.read(15),b''):			
			ret.append(delim.join([f'{byte:08b}' for byte in chunk]))			
	for up_el in ret:
		i=i+1
		print('Work with element # '+str(ret.index(up_el)))
		for down_el in up_el:
			if down_el=='0':				
				new=new+'-'				
			else:				
				new=new+'*'									
		print('New element '+new)
		view.append(new)
		new=''
	print("all "+str(i)+" elements in ret")
	return view

 

print(view_bytes('test_img.jpg'))

