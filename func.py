def func1(ds, **kwargs):
  print('before calc: ', ds)
  print('after calc: ', kwargs['macros'].ds_add(ds, 3))
  print('params', kwargs['params'])
  return 'func1'
