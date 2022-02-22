# Json-quake
### Displays map from a data.json about recent quakes

![image](https://user-images.githubusercontent.com/58234228/155048463-2f092766-ad26-45a5-8438-e9147031e58c.png)

#### Long nesting - PyCharm shows the possibilities

```python
for quake_dict in all_quake_dict:
    cordinate_x = quake_dict['geometry']['coordinates'][0]  # long nesting - debug helps
    cordinate_y = quake_dict['geometry']['coordinates'][1]
    cordinates_x.append(cordinate_x)
    cordinates_y.append(cordinate_y)
```

![debug_helps](https://user-images.githubusercontent.com/58234228/155048511-abdd4d2b-da49-48a5-8f57-f419ca94c6af.PNG)
