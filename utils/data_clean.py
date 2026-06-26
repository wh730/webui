from utils.config import api_client

class DataPrepareClean:
    @staticmethod
    def init_test_data():
        """【前置工作】所有用例执行前：清理历史脏数据、初始化干净测试资源"""
        print("===== 执行用例前置：清理历史脏数据，初始化测试数据 =====")
        # 示例1：删除上一轮残留的测试圈子（避免重复创建重名报错）
        # api_client.delete("/circle/delete_test_data")
        # 示例2：创建专属本轮测试临时账号/圈子
        # api_client.post("/circle/create_temp_resource")
        pass

    @staticmethod
    def clear_test_data():
        """【后置清理】全部用例跑完：删除本次生成的所有测试数据"""
        print("===== 执行用例后置：清理本轮全部测试脏数据 =====")
        # 示例：删除本次自动化创建的圈子、用户资源
        # api_client.delete("/circle/del_all_temp_circle")
        pass