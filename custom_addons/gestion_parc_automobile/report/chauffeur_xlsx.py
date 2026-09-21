from odoo import models


class ChauffeurXlsx(models.AbstractModel):
    _name = 'report.gestion_parc_automobile.chauffeur_xlsx'
    _inherit = 'report.report_xlsx.abstract'
    _description = 'Rapport Excel des chauffeurs'

    def generate_xlsx_report(self, workbook, data, wizard):

        year = data.get('year')
        month = data.get('month')

        months = {
            '1': 'JANVIER',
            '2': 'FEVRIER',
            '3': 'MARS',
            '4': 'AVRIL',
            '5': 'MAI',
            '6': 'JUIN',
            '7': 'JUILLET',
            '8': 'AOUT',
            '9': 'SEPTEMBRE',
            '10': 'OCTOBRE',
            '11': 'NOVEMBRE',
            '12': 'DECEMBRE',
        }

        month_name = months.get(str(month), '')

        # =====================================================
        # EMPLOYES
        # =====================================================

        employees = self.env['hr.employee'].search(
            [],
            order='name asc'
        )

        # =====================================================
        # FEUILLE EXCEL
        # =====================================================

        sheet = workbook.add_worksheet(
            f'DNS_{month_name}_{year}'[:31]
        )

        # =====================================================
        # FORMATS
        # =====================================================

        titre_format = workbook.add_format({
            'bold': True,
            'font_size': 12,
            'align': 'left',
            'valign': 'vcenter',
        })

        header_format = workbook.add_format({
            'bold': True,
            'border': 1,
            'align': 'center',
            'valign': 'vcenter',
            'text_wrap': True,
            'bg_color': '#D9E1F2',
        })

        label_format = workbook.add_format({
            'bold': True,
            'border': 1,
            'align': 'left',
            'valign': 'vcenter',
        })

        valeur_format = workbook.add_format({
            'border': 1,
            'align': 'left',
            'valign': 'vcenter',
        })

        number_format = workbook.add_format({
            'border': 1,
            'align': 'right',
            'valign': 'vcenter',
            'num_format': '#,##0.00',
        })

        presence_format = workbook.add_format({
            'border': 1,
            'align': 'right',
            'valign': 'vcenter',
            'num_format': '0.00',
        })

        # =====================================================
        # LARGEUR
        # =====================================================

        sheet.set_column('A:A', 20)
        sheet.set_column('B:B', 28)
        sheet.set_column('C:C', 30)
        sheet.set_column('D:D', 22)
        sheet.set_column('E:E', 22)
        sheet.set_column('F:F', 18)
        sheet.set_column('G:G', 22)
        sheet.set_column('H:H', 12)
        sheet.set_column('I:I', 12)

        # =====================================================
        # EMPLOYEUR
        # =====================================================

        sheet.write(
            'A1',
            "Informations de l'employeur",
            titre_format
        )

        sheet.write(
            'A2',
            'NUMERO UNIQUE EMPLOYEUR',
            label_format
        )

        company = self.env.company

        employer_number = (
            company.company_registry
            or company.vat
            or ''
        )

        sheet.write(
            'B2',
            employer_number,
            valeur_format
        )

        sheet.write(
            'C2',
            'Année',
            label_format
        )

        sheet.write(
            'D2',
            year,
            valeur_format
        )

        sheet.write(
            'E2',
            'Mois',
            label_format
        )

        sheet.write(
            'F2',
            month_name,
            valeur_format
        )

        # =====================================================
        # TITRE
        # =====================================================

        sheet.write(
            'A4',
            'Informations des salariés',
            titre_format
        )

        # =====================================================
        # COLONNES
        # =====================================================

        headers = [
            'Numéro Assuré Social',
            'Prénom et Nom',
            'Type de pièce',
            'Numéro pièce',
            'Numéro passeport',
            'Type de contrat',
            'Salaire brut assujetti',
            'Présence',
            'Cadre',
        ]

        header_row = 5

        for col, header in enumerate(headers):
            sheet.write(
                header_row,
                col,
                header,
                header_format
            )

        # =====================================================
        # DONNEES
        # =====================================================

        row = header_row + 1

        for employee in employees:

            # -------------------------------------------------
            # CONTACT PROFESSIONNEL
            # -------------------------------------------------

            chauffeur = employee.work_contact_id

            # Si aucun contact professionnel
            if not chauffeur:
                continue

            # -------------------------------------------------
            # NUMERO ASSURE SOCIAL
            # -------------------------------------------------

            numero_assure_social = employee.ssnid or ''

            # -------------------------------------------------
            # NOM
            # -------------------------------------------------

            nom = employee.name or ''

            # -------------------------------------------------
            # TYPE DE PIECE
            # -------------------------------------------------

            if employee.identification_id:
                type_piece = "CARTE D'IDENTITE NATIONALE"
            elif employee.passport_id:
                type_piece = "PASSEPORT"
            else:
                type_piece = ""

            # -------------------------------------------------
            # NUMERO PIECE
            # -------------------------------------------------

            numero_piece = employee.identification_id or ''

            # -------------------------------------------------
            # NUMERO PASSEPORT
            # -------------------------------------------------

            numero_passeport = employee.passport_id or ''

            # -------------------------------------------------
            # TYPE DE CONTRAT
            # -------------------------------------------------

            type_contrat = ''

            if employee.contract_type_id:
                type_contrat = employee.contract_type_id.name

            # -------------------------------------------------
            # SALAIRE
            # -------------------------------------------------

            salaire = employee.wage or 0.0

            # -------------------------------------------------
            # PRESENCE
            # -------------------------------------------------

            presence = 0.0

            # -------------------------------------------------
            # CADRE
            # -------------------------------------------------

            cadre = ''

            # =================================================
            # ECRITURE EXCEL
            # =================================================

            sheet.write(
                row,
                0,
                numero_assure_social,
                valeur_format
            )

            sheet.write(
                row,
                1,
                nom,
                valeur_format
            )

            sheet.write(
                row,
                2,
                type_piece,
                valeur_format
            )

            sheet.write(
                row,
                3,
                numero_piece,
                valeur_format
            )

            sheet.write(
                row,
                4,
                numero_passeport,
                valeur_format
            )

            sheet.write(
                row,
                5,
                type_contrat,
                valeur_format
            )

            sheet.write_number(
                row,
                6,
                salaire,
                number_format
            )

            sheet.write_number(
                row,
                7,
                presence,
                presence_format
            )

            sheet.write(
                row,
                8,
                cadre,
                valeur_format
            )

            row += 1

        # =====================================================
        # OPTIONS EXCEL
        # =====================================================

        sheet.freeze_panes(
            header_row + 1,
            0
        )

        if row > header_row + 1:

            sheet.autofilter(
                header_row,
                0,
                row - 1,
                len(headers) - 1
            )