def minimos(x_values, y_values):
  m = len(x_values)
  media_x = sum(x_values)
  media_y = sum(y_values)
  media_pot_x = sum(list(map(lambda x: x**2, x_values)))
  media_x_y = sum(list(map(lambda x,y: x*y, x_values, y_values)))
  x2 = list(map(lambda x: x**2, x_values))
  xy = list(map(lambda x,y: x*y, x_values, y_values))
  divisor = m * media_pot_x - media_x ** 2
  
  a = round((media_pot_x * media_y - media_x_y * media_x)/divisor, 3)
  a1 = round((m * media_x_y - media_x * media_y) / divisor, 3)
  return f'f(x) = {a1} * x + {a}\n'



exemplo_x = [0, 0.25, 0.50, 0.75, 1]
exemplo_y = [1.0, 1.2840, 1.6487, 2.1170, 2.7183]
print(minimos(exemplo_x, exemplo_y))


extra_x = [1, 1.1, 1.3, 1.5, 1.9, 2.1]
extra_y = [1.84, 1.96, 2.21, 2.45, 2.94, 3.18]  
print(minimos(extra_x, extra_y))


extra_x2 = [4.0, 4.2, 4.5, 4.7, 5.1, 5.5, 5.9, 6.3, 6.8, 7.1]
extra_y2 = [102.56, 113.18, 130.11, 142.05, 167.53, 195.14, 224.87, 256.73, 299.50, 326.72]

print(minimos(extra_x2, extra_y2))