# -*- coding:utf-8 -*-
"""
-------------------------------------------------
Project Name: dl_train_form
File Name: base_converter.py
Author: gaoyw
Create Date: 2020/12/3
-------------------------------------------------
"""


class BaseDataTypeConverter(object):
    def __init__(self):
        """
        将数据格式之间来回转换，注意这里只涉及到数据转换，而不涉及到任何数据预处理
        :param raw_path: 格式等于raw_data下的数据
        :param process_path: 格式等于prepared_data下的数据
        :param dev_output_path: 格式是prepared_data下的数据并合理组织上预测的标签
        :param organized_path: 格式是任意的数据格式 但是应当包含预测标签与原始标签，如果他们之间谁缺了，就将另一个标签作为替代复制一份

        相互转换的规则：
        raw2process process2raw 无损转换
        raw2dev_out raw2organized process2dev_out process2organized 复制原始标签作为预测标签
        dev_out2raw organized2raw dev_out2process organized2process 仅保留原始标签，移除预测标签
        """
        self.mid_data = None

    def raw2mid_data(self, raw_path):
        raise NotImplementedError()

    def process2mid_data(self, process_path):
        raise NotImplementedError()

    def dev_out2mid_data(self, dev_output_path):
        raise NotImplementedError()

    def organized2mid_data(self, organized_path):
        raise NotImplementedError()

    def mid_data2raw(self, raw_path):
        raise NotImplementedError()

    def mid_data2process(self, process_path):
        raise NotImplementedError()

    def mid_data2dev_out(self, dev_output_path):
        raise NotImplementedError()

    def mid_data2organized(self, organized_path):
        raise NotImplementedError()

    def raw2process(self, raw_path, process_path):
        self.raw2mid_data(raw_path)
        self.mid_data2process(process_path)

    def process2raw(self, process_path, raw_path):
        self.process2mid_data(process_path)
        self.mid_data2raw(raw_path)

    def raw2dev_out(self, raw_path, dev_output_path):
        self.raw2mid_data(raw_path)
        self.mid_data2dev_out(dev_output_path)

    def raw2organized(self, raw_path, organized_path):
        self.raw2mid_data(raw_path)
        self.mid_data2organized(organized_path)

    def process2dev_out(self, process_path, dev_output_path):
        self.process2mid_data(process_path)
        self.mid_data2dev_out(dev_output_path)

    def process2organized(self, process_path, organized_path):
        self.process2mid_data(process_path)
        self.mid_data2organized(organized_path)

    def dev_out2raw(self, dev_output_path, raw_path):
        self.dev_out2mid_data(dev_output_path)
        self.mid_data2raw(raw_path)

    def organized2raw(self, organized_path, raw_path):
        self.organized2mid_data(organized_path)
        self.mid_data2raw(raw_path)

    def dev_out2process(self, dev_output_path, process_path):
        self.dev_out2mid_data(dev_output_path)
        self.mid_data2process(process_path)

    def organized2process(self, organized_path, process_path):
        self.organized2mid_data(organized_path)
        self.mid_data2process(process_path)

    def organized2dev_out(self, organized_path, dev_output_path):
        self.organized2mid_data(organized_path)
        self.mid_data2dev_out(dev_output_path)
