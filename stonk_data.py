class SingleStockData (object):
    def __init__(self, name, yearly_low, yearly_high) -> None:
        self._name = name
        self._yearly_low = yearly_low
        self._yearly_high = yearly_high

    def get_name(self):
        return self._name

    def get_low(self):
        return self._yearly_low
    
    def get_high(self):
        return self._yearly_high


class NASDAQStockData (object):
    def __init__(self) -> None:
        self._stock_data = []
    
    def process_file(self, file_name) -> bool:
        current_line = ""
        with open(file_name, 'r') as file:
            while not current_line:
                current_line = file.readline()
                split_line = current_line.split(",")
                name, low, high = split_line[0], float(split_line[1]), float(split_line[2])
                self._stock_data.append(SingleStockData(name, low, high))
        return True
        
    def display_file(self) -> None:
        for count, stock in enumerate(self._stock_data):
            current_stock = self._stock_data[count]
            print(f"{count + 1}. {current_stock.get_name()}\t\t${current_stock.get_low}\t\t${current_stock.get_low}")
