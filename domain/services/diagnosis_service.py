# domain/services/diagnosis_service.py
"""
Diagnóstico global del mercado.
"""

from domain.services.indicator_service import IndicatorService

class DiagnosisService:
    @staticmethod
    def get_regime(df):
        return IndicatorService.compute_regime(df)

    @staticmethod
    def get_avg_adx(df_dict):
        adx_vals = []
        for df in df_dict.values():
            adx = IndicatorService.compute_adx(df)
            if adx.value > 0:
                adx_vals.append(adx.value)
        return sum(adx_vals)/len(adx_vals) if adx_vals else 0.0
