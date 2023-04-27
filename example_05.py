en_uz_dict = {
  'apple':'olma',
  'banana':'banan',
  'cherry':'olcha',
  'pineapple':'ananas',
  'pomegranate':'anor',
  'grapes':'uzum',
}
uz_en_dict = {}
for key, value in en_uz_dict:
  uz_en_dict[value] = key
print(en_uz_dict)
print(uz_en_dict)
