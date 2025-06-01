def generate_order_id(customer_name):
  uniq_id = ""
  for i in customer_name[-3:]:
    uniq_id += f"{i}{len(customer_name)}"
  return uniq_id

print(generate_order_id("budi siregar")) 