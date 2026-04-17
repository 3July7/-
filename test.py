class Huaxiong:
    def __init__(self, initial_huaxiong=100):
        self.alive_huaxiong = initial_huaxiong # 初始华雄数量
        self.dead_huaxiong = 0 # 死去的华雄数量
        self.time_count = 0 # 记录时间步数
        self.huaxiong_kill_count = 0 # 记录关羽砍死的华雄数量

        self.guanyv = 0 # 0表示未开始，1表示正在进行
        self.guanyv_time = 0 # 关羽开始砍一只华雄的时间
        self.huatuo = 0 # 0表示未开始，1表示正在进行
        self.huatuo_time = 0 # 华佗开始救一只华雄的时间

    def guanyv_kill(self):
        if self.guanyv == 1 and self.time_count - self.guanyv_time >= 10: # 假设关羽砍一只华雄需要10个时间步
            self.alive_huaxiong -= 1 # 关羽砍死一只华雄
            self.dead_huaxiong += 1 # 关羽砍死一只华雄后，死去的华雄数量增加
            self.huaxiong_kill_count += 1 # 记录关羽砍死的华雄数量
            self.guanyv = 0 # 关羽砍完一只华雄后，重置状态
            print(f"关羽在{self.time_count}砍死了一只华雄")
        
        if self.alive_huaxiong > 0 and self.guanyv == 0:
            self.guanyv = 1 # 关羽开始砍一只华雄
            self.guanyv_time = self.time_count # 记录关羽开始砍一只华雄的时间
            print(f"关羽在{self.time_count}开始砍一只华雄")

    def huatuo_cure(self):
        if self.huatuo == 1 and self.time_count - self.huatuo_time >= 15: # 假设华佗救一只华雄需要15个时间步
            self.alive_huaxiong += 1 # 华佗救活一只华雄
            self.dead_huaxiong -= 1 # 华佗救活一只华雄后，死去的华雄数量减少
            self.huatuo = 0 # 华佗救完一只华雄后，重置状态
            print(f"华佗在{self.time_count}救活了一只华雄")

        if self.dead_huaxiong > 0 and self.huatuo == 0:
            self.huatuo = 1 # 华佗开始救一只华雄
            self.huatuo_time = self.time_count # 记录华佗开始救一只华雄的时间
            print(f"华佗在{self.time_count}开始救一只华雄")

    def main(self):
        while self.alive_huaxiong > 0:
            self.guanyv_kill()
            self.huatuo_cure()
            self.guanyv_kill() # 关羽可能在同一时间砍两只华雄
            if self.alive_huaxiong == 0: # 如果所有华雄都死了，结束循环
                break
            self.time_count += 1 # 时间步数增加

if __name__ == "__main__":
    # 设置初始华雄数量
    initial_huaxiong = 100 
    battle = Huaxiong(initial_huaxiong)
    battle.main()
    print(f"最终死去的华雄数量: {battle.huaxiong_kill_count}")
    print(f"总耗时: {battle.time_count}")