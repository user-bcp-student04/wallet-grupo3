"""Ingeniero de pruebas: edita aquí las instrucciones de revisión."""

from graph.state import WorkflowState
from graph.context import _ctx, _const_block, _feedback_block


INSTRUCTIONS = ('Ingeniero de pruebas del equipo. Realiza la tarea de tu rol.\n'

                '--ALCANCE-- \n'
                '1. Validar el logeo: comprobando ingresos con documentos no validos.\n'
                '2. Comprueba que un QR válido se genere con el comercio y los datos correctos, y que pueda leerse con la app prevista.\n'
                '3. Prueba QRs inválidos, vencidos, alterados o asociados a otro comercio; no deberían permitir cobrar.\n'
                '4. Verifica que, antes de confirmar, se muestren claramente el comercio y el importe, y que la persona pueda cancelar.\n'
                '5. Comprueba que un pago confirmado se cobre una sola vez y que repetir o volver a escanear no duplique el cargo.\n'
                '3. Validar si las cuentas pertenecer a la persona que corresponde.\n'
                '4. 6. Prueba cancelaciones, saldo insuficiente y problemas de conexión: el estado debe ser claro y no causar un cobro incierto o repetido.\n'
                '5. Validar limites y si el monto que tiene la persona corresponde al que cargo a su cuenta.\n'
                '6. Validar los estados de la cuenta, que no se encuentre bloqueada.\n'
                '9. Revisa que el historial y el comprobante reflejen el comercio, importe y estado reales.\n'
                '10. Comprueba el comprobante y que el pago aparezca una sola vez en tu historial y tenga los datos que ingresaste.\n')



def testing_node(state: WorkflowState, invoke) -> dict:
    prompt = (INSTRUCTIONS + _const_block(state, "Respeta las restricciones del proyecto y la constitución.") + "\nRepositorio: " + state["repo_name"] + "\nPlan:\n" + _ctx(state.get("out_plan", ""),2500) + "\nCódigo original:\n" + _ctx(state.get("snapshot", ""),4000) + "\nBackend:\n" + _ctx(state.get("out_backend", ""),6000) + "\nFrontend:\n" + _ctx(state.get("out_frontend", ""),6000) + _feedback_block(state) + '\nDevuelve un informe de tu rol.')
    if state.get("include_data"):
        prompt += "\nContrato aprobado de Datos y persistencia:\n" + _ctx(state.get("out_data", ""), 6000)
    return {"out_testing": invoke(prompt)}
