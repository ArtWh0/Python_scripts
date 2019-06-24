def view_bytes(fpath, delim=''):
	ret=[]
	i=1
	new=''
	with open(fpath, 'br') as f:
		for chunk in iter(lambda: f.read(20),b''):			
			ret.append(delim.join([f'{byte:08b}' for byte in chunk]))			
	for up_el in ret:
		print('Work with element # '+str(ret.index(up_el)))
		for down_el in up_el:
			if down_el=='0':				
				new=new+' '				
			else:
				
				new=new+'*'
		if new==ret[ret.index(up_el)-1]:
			i=i+1
		if i>5:
			i=0
			continue				
		print('New element '+new+' on position'+str(ret.index(up_el)))
		ret.insert(ret.index(up_el),new)
		new=''
	
	return ret
 

print(view_bytes('test_img.jpg'))
