"""Revisor de seguridad: edita aquí las instrucciones de revisión."""

from graph.state import WorkflowState
from graph.context import _ctx, _const_block, _feedback_block


INSTRUCTIONS = ('Analista de Seguridad del equipo. Realiza la tarea de tu rol.\n'
                
                '--ALCANCE--\n'
                '1. Sobre el registro: deben existir datos obligatorios y deben ser únicos (DNI para para persona natural y RUC para comercio).\n'
                '2. Sobre la autenticación: Debe existir un tiempo máximo de sesión abierta, una contraseña valida, recuperación de credenciales, expiración de sesiones o de preferencia autenticación con biometria facial o token.\n'
                '3. Acceso a Cuentas de la billetera: Restrigido y dedicado al cliente o comercio que le corresponde, no debe tener acceso a otras cuentas.\n'
                '4. Comunicación: Revisa cómo se protegen las comunicaciones y los datos, y que los registros no guarden información sensible innecesaria.\n'
                '5. Validar que los datos sensibles estén hasheados para consultas y se requieren mostrase que esten encriptados.\n'
                '6. Validar autorización: comprobar que cada usuario solo pueda consultar y operar sus propias cuentas.\n'
                '7. Define qué alertas, umbrales y medidas de respuesta se necesitan ante operaciones sospechosas o fraudulentas, que se envié un pop up\n'
                '8. Para pagar con QR de forma más segura: Verifica que el QR no exponga datos sensibles y que no sea fácil de falsificar o modificar. Que no tenga en plano los datos.\n'
                '9: Usa comunicación con https para proteger la transmisión de datos sensibles.\n'
                '10: Usar Certificados Digitales para garantizar la autenticidad y seguridad de las comunicaciones.\n'
                '11: Cuando se este operando se debe garantice el mockeo temporal y luego desbloqueo el desbloque (Ej: numero de cuenta) con la finalidad de garantizar que sea único.\n')



def security_node(state: WorkflowState, invoke) -> dict:
    prompt = (INSTRUCTIONS + _const_block(state, "Respeta las restricciones del proyecto y la constitución.") + "\nRepositorio: " + state["repo_name"] + "\nPlan:\n" + _ctx(state.get("out_plan", ""),2500) + "\nCódigo original:\n" + _ctx(state.get("snapshot", ""),4000) + "\nBackend:\n" + _ctx(state.get("out_backend", ""),6000) + "\nFrontend:\n" + _ctx(state.get("out_frontend", ""),6000) + _feedback_block(state) + '\nDevuelve un informe de tu rol.')
    if state.get("include_data"):
        prompt += "\nContrato aprobado de Datos y persistencia:\n" + _ctx(state.get("out_data", ""), 6000)
    return {"out_security": invoke(prompt)}
