from classifiers.base_classifier import BaseODSClassifier

class ODS14Classifier(BaseODSClassifier):
    def __init__(self):
        super().__init__(14)

    def get_padroes(self):
        return [
            r'marinho',
            r'oceano[s]?',
            r'mar[es]?',
            r'costa\w*',
            r'mangue',
            r'ciclo[s]? da [áa]gua',
            r'ciclo[s]? biogeoqu[íi]mico[s]?',
            r'modelo[s]? de circula[çc][ãa]o oce[âa]nica',
            r'modelagem de circula[çc][ãa]o oce[âa]nica',
            r'iceocean|oceano gelado',
            r'eutr[óo]fica\w*',
            r'marinha',
            r'branqueamento de corais',
            r'manejo|gest[ãa]o costeir[oa]',
            r'habitat[s]? costeir[oa]s?',
            r'lixo marinho',
            r'acidifica[çc][ãa]o dos oceanos',
            r'acidifica[çc][ãa]o.*[áa]gua do mar',
            r'pesca',
            r'pesca excessiva',
            r'rendimento sustent[áa]vel',
            r'[áa]rea[s]? marinha[s]? protegida[s]?',
            r'conserva[çc][ãa]o marinha',
            r'ecoturismo',
            r'conserva[çc][ãa]o baseada na comunidade',
            r'deslizamento de terra marinha',
            r'polui[çc][ãa]o marinha',
            r'escoamento de nutrientes',
            r'ecoturismo costeiro',
            r'pesca destrutiva',
            r'pesca local',
            r'pescadores artesanais',
            r'direitos de pesca',
            r'riqueza de esp[ée]cies',
            r'conhecimento ecol[óo]gico tradicional',
            r'pequenas ilhas em desenvolvimento',
            r'cota marinha',
            r'economia marinha',
            r'pol[íi]tica marinha'
        ]