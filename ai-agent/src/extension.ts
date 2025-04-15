import * as vscode from 'vscode';
import * as path from 'path';

export function activate(context: vscode.ExtensionContext) {
    let disposable = vscode.commands.registerCommand('aiagent.run', () => {
        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders) {
            vscode.window.showErrorMessage('No workspace is open!');
            return;
        }

        const workspaceRoot = workspaceFolders[0].uri.fsPath;
        const scriptPath = path.join(workspaceRoot, 'main.py');

        const terminal = vscode.window.createTerminal(`AI Agent`);
        terminal.show();
        terminal.sendText(`python "${scriptPath}"`);
    });

    context.subscriptions.push(disposable);
}

export function deactivate() {}
