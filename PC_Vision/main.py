def view_bytes(fpath, delim=''):
	ret=[]
	i=1
	with open(fpath, 'br') as f:
		for chunk in iter(lambda: f.read(20),b''):			
			ret.append(delim.join([f'{byte:08b}' for byte in chunk]))
			i=i+1
	for up_el in ret:
		for down_el in up_el:
			if down_el=='0':
				ret[ret.index(up_el)][up_el.index(down_el)]=' '
			else:
				ret[ret.index(up_el)][up_el.index(down_el)]='*'
	return ret
 

print(view_bytes('test_img.jpg'))
