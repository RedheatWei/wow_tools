#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/11/28 17:44
# @Author  : unknown
import ctypes
import json
from ctypes import Structure, c_uint32, c_int32, c_float, c_char


class SpellRecord(Structure):
    _fields_ = [
        ('ID', c_int32),
        ('Category', c_uint32),
        ('DispelType', c_uint32),
        ('Mechanic', c_uint32),
        ('Attributes', c_uint32),
        ('AttributesEx', c_uint32),
        ('AttributesEx2', c_uint32),
        ('AttributesEx3', c_uint32),
        ('AttributesEx4', c_uint32),
        ('AttributesEx5', c_uint32),
        ('AttributesEx6', c_uint32),
        ('AttributesEx7', c_uint32),
        ('ShapeshiftMask', c_uint32),
        ('unk_320_2', c_int32),
        ('ShapeshiftExclude', c_uint32),
        ('unk_320_3', c_int32),
        ('Targets', c_uint32),
        ('TargetCreatureType', c_uint32),
        ('RequiresSpellFocus', c_uint32),
        ('FacingCasterFlags', c_uint32),
        ('CasterAuraState', c_uint32),
        ('TargetAuraState', c_uint32),
        ('ExcludeCasterAuraState', c_uint32),
        ('ExcludeTargetAuraState', c_uint32),
        ('CasterAuraSpell', c_uint32),
        ('TargetAuraSpell', c_uint32),
        ('ExcludeCasterAuraSpell', c_uint32),
        ('ExcludeTargetAuraSpell', c_uint32),
        ('CastingTimeIndex', c_uint32),
        ('RecoveryTime', c_uint32),
        ('CategoryRecoveryTime', c_uint32),
        ('InterruptFlags', c_uint32),
        ('AuraInterruptFlags', c_uint32),
        ('ChannelInterruptFlags', c_uint32),
        ('ProcTypeMask', c_uint32),
        ('ProcChance', c_uint32),
        ('ProcCharges', c_uint32),
        ('MaxLevel', c_uint32),
        ('BaseLevel', c_uint32),
        ('SpellLevel', c_uint32),
        ('DurationIndex', c_uint32),
        ('PowerType', c_int32),
        ('ManaCost', c_uint32),
        ('ManaCostPerLevel', c_uint32),
        ('ManaPerSecond', c_uint32),
        ('ManaPerSecondPerLevel', c_uint32),
        ('RangeIndex', c_uint32),
        ('Speed', c_float),
        ('ModalNextSpell', c_uint32),
        ('CumulativeAura', c_uint32),
        ('Totem_1', c_uint32),
        ('Totem_2', c_uint32),
        ('Reagent_1', c_int32),
        ('Reagent_2', c_int32),
        ('Reagent_3', c_int32),
        ('Reagent_4', c_int32),
        ('Reagent_5', c_int32),
        ('Reagent_6', c_int32),
        ('Reagent_7', c_int32),
        ('Reagent_8', c_int32),
        ('ReagentCount_1', c_int32),
        ('ReagentCount_2', c_int32),
        ('ReagentCount_3', c_int32),
        ('ReagentCount_4', c_int32),
        ('ReagentCount_5', c_int32),
        ('ReagentCount_6', c_int32),
        ('ReagentCount_7', c_int32),
        ('ReagentCount_8', c_int32),
        ('EquippedItemClass', c_int32),
        ('EquippedItemSubclass', c_int32),
        ('EquippedItemInvTypes', c_int32),
        ('Effect_1', c_uint32),
        ('Effect_2', c_uint32),
        ('Effect_3', c_uint32),
        ('EffectDieSides_1', c_int32),
        ('EffectDieSides_2', c_int32),
        ('EffectDieSides_3', c_int32),
        ('EffectRealPointsPerLevel_1', c_float),
        ('EffectRealPointsPerLevel_2', c_float),
        ('EffectRealPointsPerLevel_3', c_float),
        ('EffectBasePoints_1', c_int32),
        ('EffectBasePoints_2', c_int32),
        ('EffectBasePoints_3', c_int32),
        ('EffectMechanic_1', c_uint32),
        ('EffectMechanic_2', c_uint32),
        ('EffectMechanic_3', c_uint32),
        ('ImplicitTargetA_1', c_uint32),
        ('ImplicitTargetA_2', c_uint32),
        ('ImplicitTargetA_3', c_uint32),
        ('ImplicitTargetB_1', c_uint32),
        ('ImplicitTargetB_2', c_uint32),
        ('ImplicitTargetB_3', c_uint32),
        ('EffectRadiusIndex_1', c_uint32),
        ('EffectRadiusIndex_2', c_uint32),
        ('EffectRadiusIndex_3', c_uint32),
        ('EffectAura_1', c_uint32),
        ('EffectAura_2', c_uint32),
        ('EffectAura_3', c_uint32),
        ('EffectAuraPeriod_1', c_uint32),
        ('EffectAuraPeriod_2', c_uint32),
        ('EffectAuraPeriod_3', c_uint32),
        ('EffectMultipleValue_1', c_float),
        ('EffectMultipleValue_2', c_float),
        ('EffectMultipleValue_3', c_float),
        ('EffectChainTargets_1', c_uint32),
        ('EffectChainTargets_2', c_uint32),
        ('EffectChainTargets_3', c_uint32),
        ('EffectItemType_1', c_uint32),
        ('EffectItemType_2', c_uint32),
        ('EffectItemType_3', c_uint32),
        ('EffectMiscValue_1', c_int32),
        ('EffectMiscValue_2', c_int32),
        ('EffectMiscValue_3', c_int32),
        ('EffectMiscValueB_1', c_int32),
        ('EffectMiscValueB_2', c_int32),
        ('EffectMiscValueB_3', c_int32),
        ('EffectTriggerSpell_1', c_uint32),
        ('EffectTriggerSpell_2', c_uint32),
        ('EffectTriggerSpell_3', c_uint32),
        ('EffectPointsPerCombo_1', c_float),
        ('EffectPointsPerCombo_2', c_float),
        ('EffectPointsPerCombo_3', c_float),
        ('EffectSpellClassMaskA_1', c_uint32),
        ('EffectSpellClassMaskA_2', c_uint32),
        ('EffectSpellClassMaskA_3', c_uint32),
        ('EffectSpellClassMaskB_1', c_uint32),
        ('EffectSpellClassMaskB_2', c_uint32),
        ('EffectSpellClassMaskB_3', c_uint32),
        ('EffectSpellClassMaskC_1', c_uint32),
        ('EffectSpellClassMaskC_2', c_uint32),
        ('EffectSpellClassMaskC_3', c_uint32),
        ('SpellVisualID_1', c_uint32),
        ('SpellVisualID_2', c_uint32),
        ('SpellIconID', c_uint32),
        ('ActiveIconID', c_uint32),
        ('SpellPriority', c_uint32),
        ('Name_Lang_enUS', c_int32),
        ('Name_Lang_enGB', c_int32),
        ('Name_Lang_koKR', c_int32),
        ('Name_Lang_frFR', c_int32),
        ('Name_Lang_deDE', c_int32),
        ('Name_Lang_enCN', c_int32),
        ('Name_Lang_zhCN', c_int32),
        ('Name_Lang_enTW', c_int32),
        ('Name_Lang_zhTW', c_int32),
        ('Name_Lang_esES', c_int32),
        ('Name_Lang_esMX', c_int32),
        ('Name_Lang_ruRU', c_int32),
        ('Name_Lang_ptPT', c_int32),
        ('Name_Lang_ptBR', c_int32),
        ('Name_Lang_itIT', c_int32),
        ('Name_Lang_Unk', c_int32),
        ('Name_Lang_Mask', c_uint32),
        ('NameSubtext_Lang_enUS', c_int32),
        ('NameSubtext_Lang_enGB', c_int32),
        ('NameSubtext_Lang_koKR', c_int32),
        ('NameSubtext_Lang_frFR', c_int32),
        ('NameSubtext_Lang_deDE', c_int32),
        ('NameSubtext_Lang_enCN', c_int32),
        ('NameSubtext_Lang_zhCN', c_int32),
        ('NameSubtext_Lang_enTW', c_int32),
        ('NameSubtext_Lang_zhTW', c_int32),
        ('NameSubtext_Lang_esES', c_int32),
        ('NameSubtext_Lang_esMX', c_int32),
        ('NameSubtext_Lang_ruRU', c_int32),
        ('NameSubtext_Lang_ptPT', c_int32),
        ('NameSubtext_Lang_ptBR', c_int32),
        ('NameSubtext_Lang_itIT', c_int32),
        ('NameSubtext_Lang_Unk', c_int32),
        ('NameSubtext_Lang_Mask', c_uint32),
        ('Description_Lang_enUS', c_int32),
        ('Description_Lang_enGB', c_int32),
        ('Description_Lang_koKR', c_int32),
        ('Description_Lang_frFR', c_int32),
        ('Description_Lang_deDE', c_int32),
        ('Description_Lang_enCN', c_int32),
        ('Description_Lang_zhCN', c_int32),
        ('Description_Lang_enTW', c_int32),
        ('Description_Lang_zhTW', c_int32),
        ('Description_Lang_esES', c_int32),
        ('Description_Lang_esMX', c_int32),
        ('Description_Lang_ruRU', c_int32),
        ('Description_Lang_ptPT', c_int32),
        ('Description_Lang_ptBR', c_int32),
        ('Description_Lang_itIT', c_int32),
        ('Description_Lang_Unk', c_int32),
        ('Description_Lang_Mask', c_uint32),
        ('AuraDescription_Lang_enUS', c_int32),
        ('AuraDescription_Lang_enGB', c_int32),
        ('AuraDescription_Lang_koKR', c_int32),
        ('AuraDescription_Lang_frFR', c_int32),
        ('AuraDescription_Lang_deDE', c_int32),
        ('AuraDescription_Lang_enCN', c_int32),
        ('AuraDescription_Lang_zhCN', c_int32),
        ('AuraDescription_Lang_enTW', c_int32),
        ('AuraDescription_Lang_zhTW', c_int32),
        ('AuraDescription_Lang_esES', c_int32),
        ('AuraDescription_Lang_esMX', c_int32),
        ('AuraDescription_Lang_ruRU', c_int32),
        ('AuraDescription_Lang_ptPT', c_int32),
        ('AuraDescription_Lang_ptBR', c_int32),
        ('AuraDescription_Lang_itIT', c_int32),
        ('AuraDescription_Lang_Unk', c_int32),
        ('AuraDescription_Lang_Mask', c_uint32),
        ('ManaCostPct', c_uint32),
        ('StartRecoveryCategory', c_uint32),
        ('StartRecoveryTime', c_uint32),
        ('MaxTargetLevel', c_uint32),
        ('SpellClassSet', c_uint32),
        ('SpellClassMask_1', c_uint32),
        ('SpellClassMask_2', c_uint32),
        ('SpellClassMask_3', c_uint32),
        ('MaxTargets', c_uint32),
        ('DefenseType', c_uint32),
        ('PreventionType', c_uint32),
        ('StanceBarOrder', c_uint32),
        ('EffectChainAmplitude_1', c_float),
        ('EffectChainAmplitude_2', c_float),
        ('EffectChainAmplitude_3', c_float),
        ('MinFactionID', c_uint32),
        ('MinReputation', c_uint32),
        ('RequiredAuraVision', c_uint32),
        ('RequiredTotemCategoryID_1', c_uint32),
        ('RequiredTotemCategoryID_2', c_uint32),
        ('RequiredAreasID', c_int32),
        ('SchoolMask', c_uint32),
        ('RuneCostID', c_uint32),
        ('SpellMissileID', c_uint32),
        ('PowerDisplayID', c_int32),
        ('EffectBonusMultiplier_1', c_float),
        ('EffectBonusMultiplier_2', c_float),
        ('EffectBonusMultiplier_3', c_float),
        ('SpellDescriptionVariableID', c_uint32),
        ('SpellDifficultyID', c_uint32),
    ]
    _pack_ = 1


class DBCHeader(Structure):
    _fields_ = [
        ('magic', c_uint32),
        ('record_count', c_uint32),
        ('field_count', c_uint32),
        ('record_size', c_uint32),
        ('string_block_size', c_uint32),
    ]
    _pack_ = 1


class DBCFile(object):
    """通用的 DBC 文件读写类"""

    WDBC_MAGIC = 1128416343

    def __init__(self, record_type):
        self.header = DBCHeader()
        self.record_type = record_type
        self.records = []
        self.string_block = b""
        self.string_table = {}  # 字符串查找表

    def read_file(self, filename):
        """读取 DBC 文件"""
        with open(filename, 'rb') as f:
            # 读取文件头
            f.readinto(self.header)

            # 验证魔数
            if self.header.magic != self.WDBC_MAGIC:
                raise ValueError(f"无效的DBC文件，魔数不匹配: {self.header.magic}")

            # 验证记录大小
            expected_size = ctypes.sizeof(self.record_type)
            if self.header.record_size != expected_size:
                print(f"警告: 记录大小不匹配，文件:{self.header.record_size}, 预期:{expected_size}")

            # 读取记录
            self.records = []
            for _ in range(self.header.record_count):
                record = self.record_type()
                f.readinto(record)
                self.records.append(record)

            # 读取字符串块
            self.string_block = f.read(self.header.string_block_size)

            # 构建字符串查找表
            self._build_string_table()

    def _build_string_table(self):
        """构建字符串偏移量查找表"""
        self.string_table = {}
        if not self.string_block:
            return

        offset = 0
        while offset < len(self.string_block):
            # 找到字符串终止符
            end = self.string_block.find(b'\x00', offset)
            if end == -1:
                break

            string_data = self.string_block[offset:end]
            try:
                string_value = string_data.decode('utf-8')
                self.string_table[offset] = string_value
            except UnicodeDecodeError:
                # 尝试其他编码
                string_value = string_data.decode('latin-1')
                self.string_table[offset] = string_value

            offset = end + 1

    def get_string(self, string_ref):
        """根据字符串引用获取实际字符串"""
        if string_ref >= len(self.string_block):
            return f"<无效引用: 0x{string_ref:08X}>"

        # 查找字符串
        if string_ref in self.string_table:
            return self.string_table[string_ref]

        # 如果不在表中，直接解析
        end = self.string_block.find(b'\x00', string_ref)
        if end == -1:
            string_data = self.string_block[string_ref:]
        else:
            string_data = self.string_block[string_ref:end]

        try:
            return string_data.decode('utf-8')
        except UnicodeDecodeError:
            return string_data.decode('latin-1', errors='replace')

    def write_file(self, filename, records=None, strings=None):
        """写入 DBC 文件"""
        if records is not None:
            self.records = records

        # 构建字符串块
        if strings is not None:
            self.string_block, string_offsets = self._build_string_block(strings)
        else:
            self.string_block = self._build_string_block_from_records()

        # 更新文件头
        self.header.magic = self.WDBC_MAGIC
        self.header.record_count = len(self.records)
        self.header.field_count = len(self.record_type._fields_)
        self.header.record_size = ctypes.sizeof(self.record_type)
        self.header.string_block_size = len(self.string_block)

        # 写入文件
        with open(filename, 'wb') as f:
            # 写入文件头
            f.write(self.header)

            # 写入记录
            for record in self.records:
                f.write(record)

            # 写入字符串块
            f.write(self.string_block)

    @staticmethod
    def _build_string_block(strings):
        """从字符串列表构建字符串块"""
        string_block = b""
        offsets = {}

        for string in strings:
            offsets[string] = len(string_block)
            encoded = string.encode('utf-8') + b'\x00'
            string_block += encoded

        return string_block, offsets

    def _build_string_block_from_records(self):
        """从记录中提取字符串构建字符串块"""
        all_strings = set()

        # 收集所有字符串引用对应的字符串
        for record in self.records:
            for field_name, field_type in self.record_type._fields_:
                if field_type == c_uint32:
                    string_ref = getattr(record, field_name)
                    if string_ref > 0:  # 有效的字符串引用
                        string_val = self.get_string(string_ref)
                        all_strings.add(string_val)

        # 构建字符串块
        string_block = b""
        for string in sorted(all_strings):  # 排序以保证一致性
            encoded = string.encode('utf-8') + b'\x00'
            string_block += encoded

        return string_block

    def __repr__(self):
        return (f"DBCFile(header={self.header}, "
                f"records={len(self.records)}, string_block={len(self.string_block)} bytes)")


if __name__ == "__main__":
    dbc_reader = DBCFile(SpellRecord)
    dbc_reader.read_file("./data/dbc/Spell.dbc")
