// Generated from ./DotLang.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link DotLangParser}.
 */
public interface DotLangListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link DotLangParser#program}.
	 * @param ctx the parse tree
	 */
	void enterProgram(DotLangParser.ProgramContext ctx);
	/**
	 * Exit a parse tree produced by {@link DotLangParser#program}.
	 * @param ctx the parse tree
	 */
	void exitProgram(DotLangParser.ProgramContext ctx);
	/**
	 * Enter a parse tree produced by {@link DotLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void enterStatement(DotLangParser.StatementContext ctx);
	/**
	 * Exit a parse tree produced by {@link DotLangParser#statement}.
	 * @param ctx the parse tree
	 */
	void exitStatement(DotLangParser.StatementContext ctx);
	/**
	 * Enter a parse tree produced by {@link DotLangParser#declVector}.
	 * @param ctx the parse tree
	 */
	void enterDeclVector(DotLangParser.DeclVectorContext ctx);
	/**
	 * Exit a parse tree produced by {@link DotLangParser#declVector}.
	 * @param ctx the parse tree
	 */
	void exitDeclVector(DotLangParser.DeclVectorContext ctx);
	/**
	 * Enter a parse tree produced by {@link DotLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(DotLangParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by {@link DotLangParser#assignment}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(DotLangParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by {@link DotLangParser#vectorLiteral}.
	 * @param ctx the parse tree
	 */
	void enterVectorLiteral(DotLangParser.VectorLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link DotLangParser#vectorLiteral}.
	 * @param ctx the parse tree
	 */
	void exitVectorLiteral(DotLangParser.VectorLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link DotLangParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void enterPrintStmt(DotLangParser.PrintStmtContext ctx);
	/**
	 * Exit a parse tree produced by {@link DotLangParser#printStmt}.
	 * @param ctx the parse tree
	 */
	void exitPrintStmt(DotLangParser.PrintStmtContext ctx);
}